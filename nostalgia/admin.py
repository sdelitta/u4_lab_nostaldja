from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Decade, Fad

admin.site.register(Decade)
admin.site.register(Fad)