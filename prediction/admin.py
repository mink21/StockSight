from django.contrib import admin
from .models import Company
from .models import Options

admin.site.register(Company)
admin.site.register(Options)