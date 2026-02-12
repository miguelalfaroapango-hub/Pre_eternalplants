from django.urls import path
from catalogo.views import*


urlpatterns = [
    path("", home, name="home"),
]
