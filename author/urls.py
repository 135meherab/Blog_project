from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_author, name= 'author_page')
]
