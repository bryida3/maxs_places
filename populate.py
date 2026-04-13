import pathlib
import django
from django.core.files import File
import os
from datetime import datetime
from bs4 import BeautifulSoup
import shutil

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'maxsplaces.settings')
django.setup()

from sites.models import Site
from sites.models import Municipality
Site.objects.all().delete()


ns = pathlib.Path("../")

files = list(filter(lambda x: not str(x).endswith("images.html") and not str(x.name).startswith("._"), list(ns.rglob("*.html"))))

j = 0
for fp in files:
    print(fp)
    with fp.open() as f:
        soup = BeautifulSoup(f, 'lxml')
        
        
        
    name = soup.find('meta', attrs={'name':'CommonName'})["content"] #name
    mun = fp.parts[1] #mun
    
    if mun.startswith("town"):
        city = mun #city if mun is a town
    else:
        city = fp.parts[2].split("_")[2] #city
    
    address = soup.find('meta', attrs={'name':'Location'})["content"] #address
    
    try: latitude = soup.find('meta', attrs={'name':'PlaceLatitude'})["content"] #latitude
    except: latitude = None
    try: longitude = soup.find('meta', attrs={'name':'PlaceLongitude'})["content"] #longitude
    except: longitude = None
    
    try:
        construction = soup.find('meta', attrs={'name':'ConstructionDate'})["content"]
        construction = construction.split(" to ")
        construction = datetime.strptime(construction[0], '%Y/%m/%d').date() #construction
        
    except: construction = None
    
    
    recognized = datetime.strptime(soup.find(id = "ContentPlaceHolderDefault_ContentPlaceHolderDefault_ContentPlaceHolderDefault_ContentPlaceHolderDefault_PlacePage1_lblFormallyRecognized").string, '%Y/%m/%d').date() #recognized
            
    
    try: image0text = soup.find(id="ContentPlaceHolderDefault_ContentPlaceHolderDefault_ContentPlaceHolderDefault_ContentPlaceHolderDefault_PlacePage1_imgImage1")["title"]
    except: image0text = ""
    try: image1text = soup.find(id="ContentPlaceHolderDefault_ContentPlaceHolderDefault_ContentPlaceHolderDefault_ContentPlaceHolderDefault_PlacePage1_imgImage2")["title"]
    except: image1text = ""
    try: image2text = soup.find(id="ContentPlaceHolderDefault_ContentPlaceHolderDefault_ContentPlaceHolderDefault_ContentPlaceHolderDefault_PlacePage1_imgImage3")["title"]
    except: image2text = ""
            
    listings = []
    listings += soup.find_all('div', attrs={'class':'listing'})
    listings += soup.find_all('div', attrs={'class':'listing hidewithjs'})
    
    significance = ' '.join([str(e) for e in listings[0].contents]) #significance
    recognition = ' '.join([str(e) for e in listings[1].contents]) #recognition
    historical = ' '.join([str(e) for e in listings[2].contents]) #historical
    additional = ' '.join([str(e) for e in listings[3].contents]) #additional
    
    
    try: municipality = Municipality.objects.filter(short_name=mun)[0]
    except:
        municipality = Municipality(short_name=mun)
        municipality.save()
    print(municipality)
    
    site = Site(name=name, mun=municipality, city=city, address=address, latitude=latitude, longitude=longitude, construction=construction, recognized=recognized, image0text=image0text, image1text=image1text, image2text=image2text, significance=significance, recognition=recognition, historical=historical, additional=additional)
    
    
    dir = fp.parent
    jpgs = list(dir.glob("*.jpg"))
    try:
        img_name = jpgs[0].name
        with open(jpgs[0], 'rb') as f:
            image = File(f)
            site.image0.save('images/' + img_name, image)
    except: pass
    try:
        img_name = jpgs[1].name
        with open(jpgs[1], 'rb') as f:
            image = File(f)
            site.image1.save('images/' + img_name, image)
    except: pass
    try:
        img_name = jpgs[2].name
        with open(jpgs[2], 'rb') as f:
            image = File(f)
            site.image2.save('images/' + img_name, image)
    except: pass
    

    
    site.save()
    j += 1
    print(j)
    
    
