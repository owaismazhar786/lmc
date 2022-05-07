import sre_compile
from django.contrib import admin
from . models import *
from embed_video.admin import AdminVideoMixin

admin.site.site_header = 'Welcome, to Labbaik Media Cell Dashboard'


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Video, MyModelAdmin)


@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject')
    search_fields = ('name', 'email')

@admin.register(Developer)
class developerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'message')