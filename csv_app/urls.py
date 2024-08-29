from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'), 
    path('generate-csv/', views.generate_csv, name='generate_csv'), 
]
