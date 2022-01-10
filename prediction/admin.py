from django.contrib import admin
from .models import Company
from .models import Options
from .models import Source

admin.site.register(Company)
admin.site.register(Options)
admin.site.register(Source)