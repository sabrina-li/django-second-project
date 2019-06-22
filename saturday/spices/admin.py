from django.contrib import admin

# Register your models here.
from .models import SpiceMixes, Spice

admin.site.register(Spice)
admin.site.register(SpiceMixes)