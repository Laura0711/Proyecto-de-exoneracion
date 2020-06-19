from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id_renta>', views.devolver, name='devolver'),
]