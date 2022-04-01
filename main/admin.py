from django.contrib import admin
from . models import Contact
from embed_video.admin import AdminVideoMixin
from .models import Videos

admin.site.site_header = 'Welcome, to Admin Dashboard'


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Videos, MyModelAdmin)
admin.site.register(Contact)
