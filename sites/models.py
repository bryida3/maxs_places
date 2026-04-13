from django.db import models

class Municipality(models.Model):
    short_name = models.CharField(max_length=50)
    long_name = models.CharField(max_length=100)
    def __str__(self):
        return self.long_name
    
class Site(models.Model):
    name = models.CharField(max_length=150)
    mun = models.ForeignKey(Municipality, on_delete=models.PROTECT)
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=150, blank=True)
    latitude = models.DecimalField(max_digits=10,decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10,decimal_places=6, null=True, blank=True)
    construction = models.DateField(null=True, blank=True)
    recognized = models.DateField(null=True, blank=True)
    image0 = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image0text = models.CharField(max_length=250, blank=True)
    image1text = models.CharField(max_length=250, blank=True)
    image2text = models.CharField(max_length=250, blank=True)
    significance = models.TextField()
    recognition = models.TextField()
    historical = models.TextField()
    additional= models.TextField()
    def __str__(self):
        return self.name
    
