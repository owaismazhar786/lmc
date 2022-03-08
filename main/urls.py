from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='Homepage'),
    path("about/", views.about, name="About"),
    path("blog/", views.blog, name="Blog"),
    path("gallery/", views.gallery, name="Gallery"),
    path("shop/", views.shop, name="Shop"),
    path("contact", views.contact, name="Contact"),
]
