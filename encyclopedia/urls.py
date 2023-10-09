from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
    path("<str:word>",views.content_entry, name="content_entry")
]
