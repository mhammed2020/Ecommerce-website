from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name="index"),
    path('details/<int:id>/', views.details, name="details"),

]
