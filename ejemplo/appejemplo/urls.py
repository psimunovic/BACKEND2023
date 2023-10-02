from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.appejemplo, name='ejemplo'),
   path('app2/', views.appejemplo2, name='ejemplo2'),
]
