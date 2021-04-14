from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_all, name="index"),
    path('add/', views.add, name="add"),
    path('stats/', views.stats, name="stats"),
    path('<unique_squirrel_id>/', views.edit, name="edit"),
]
