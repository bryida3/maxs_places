from django.contrib import admin

from .models import Site
from .models import Municipality

admin.site.register(Site)
admin.site.register(Municipality)
