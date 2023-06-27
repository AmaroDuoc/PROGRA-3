from django.urls import path
from . views import login,login2,index,catalogo,autos,crud_motos,agregar_motos,borrar_moto,modificar_moto,motos,motoUpdate,contactos,carrito

urlpatterns=[
    path('login', login, name="login"),
    path('login2/', login2, name="login2"),
    path('', index, name="index"),
    path('catalogo/', catalogo, name="catalogo"),
    path('autos/', autos, name="autos"),
    path('crud_motos/',crud_motos,name="crud_motos"),
    path('agregar_motos/',agregar_motos, name="agregar_motos"),
    path('borrar_moto/<str:pk>',borrar_moto, name="borrar_moto"),
    path('modificar_moto/<str:pk>',modificar_moto,name="modificar_moto"),
    path('motoUpdate/',motoUpdate,name="motoUpdate"),
    path('motos/', motos, name="motos"),
    path('contactos/', contactos, name="contactos"),
    path('carrito/', carrito, name="carrito"),

] 