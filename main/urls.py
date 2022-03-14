from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='Homepage'),
    path("about/", views.about, name="About"),
    path("blog/", include('blog.urls'), name="Blog"),
    path("gallery/", views.gallery, name="Gallery"),
    path("service/", views.service, name="Services"),
    path("contact", views.contact, name="Contact"),
]
