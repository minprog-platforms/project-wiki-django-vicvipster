from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/", views.entry, name="entry"),
    path("new_page/", views.new, name="new"),
    path("random/", views.random, name="random"),
    path("new_entry/", views.new_entry, name="new_entry"),
    path("search_results/", views.search_results, name="search_results"),
    path("edit", views.edit, name="edit")
]
