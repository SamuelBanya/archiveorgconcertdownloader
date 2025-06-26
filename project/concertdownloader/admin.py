from django.contrib import admin

# Register your models here.
from .models import Concert, Band 

admin.site.register(Concert)
admin.site.register(Band)
