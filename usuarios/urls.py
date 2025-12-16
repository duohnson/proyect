from django.urls import path # Obligatorio en todas las apps o modulos.
from . import views # Importamos views de la carpeta home, ya que el . es igual a ./home/ y solicitamos a views

urlpatterns = [
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), 
    path('perfil/', views.perfil_view, name='perfil'),
]

'''

NoReverseMatch - En caso de este error, revise name='nombre de app' 
en ruta urls y que tenga coincidencia con views.

'''