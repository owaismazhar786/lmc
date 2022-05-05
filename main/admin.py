from django.contrib import admin
from . models import *
from embed_video.admin import AdminVideoMixin

admin.site.site_header = 'Welcome, to Labbaik Media Cell Dashboard'


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Video, MyModelAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')

admin.site.register(Contact)

admin.site.register(Developer)

class developerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')