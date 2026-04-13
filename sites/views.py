from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Site
from .models import Municipality


def index(request):
    context = {"municipalities": Municipality.objects.all().order_by("long_name")}
    print(context)
    return render(request, "sites/index.html", context)
    
def municipality(request, mun):
    municipality = Municipality.objects.filter(short_name=mun)[0]
    places_in_mun = municipality.site_set.all()
    context = {"places_in_mun": places_in_mun, "mun": municipality}
    return render(request, "sites/mun.html", context)

def place(request, id):
    place = Site.objects.get(pk=id)
    context = {"place": place}
    return render(request, "sites/site.html", context)
