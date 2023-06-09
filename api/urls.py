from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.get_route, name='get_route'),
    path("notes/", views.get_notes, name="notes"),
    path("notes/create", views.create_note, name="create-note"),
    path("notes/<str:pk>", views.get_note, name="note"),
    path("notes/<str:pk>/update", views.update_note, name="update-note"),
    path("notes/<str:pk>/delete", views.delete_note, name="delete-note"),

]
