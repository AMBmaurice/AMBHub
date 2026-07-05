from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_connexion, name='connexion'),
    path('hub/', views.page_hub, name='hub'),
    path('logout/', views.page_deconnexion, name='deconnexion'),

]
