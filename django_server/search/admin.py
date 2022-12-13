from django.contrib import admin

# Register your models here.

from search.models import Archive, SecteurDActivit, Service

admin.site.register(Archive)
admin.site.register(SecteurDActivit)
admin.site.register(Service)
