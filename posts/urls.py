from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_post, name="post_page"),
    path('edit/<int:id>', views.edit_post, name="edit_post"),
    path('delete/<int:id>', views.delete_post, name="delete_post")
]
