from django.shortcuts import render
from .models import Auto, Motocicleta, tipo_vehiculo
#from .serializers import AutoSerializer, MotocicletaSerializer

## Elementos para la generacion de la api
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status 
from rest_framework.parsers import JSONParser
# Elementos para la autenticacion
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#@permission_classes((IsAuthenticated,))
def index(request):
    return render(request, "core/index.html")

def login(request):
    return render(request, "core/login.html")


def login2(request):
    return render(request, "core/login2.html")


def catalogo(request):
    return render(request, "core/catalogo.html")


def contactos(request):
    return render(request, "core/contactos.html")


def carrito(request):
    return render(request, "core/carrito.html")


def autos(request):
    return render(request, "core/autos.html")


def motos(request):
    return render(request, "core/motos.html")

def crud_motos(request):
    motos=Motocicleta.objects.all()
    context={'motos':motos}
    return render(request,'core/lista_moto.html', context)

def agregar_motos(request):
    if request.method != "POST":
        tvehi=tipo_vehiculo.objects.all()
        context={'tvehi':tvehi}
        return render(request,'core/añadirmoto.html', context)
    
    else:
        patente=request.POST["patente"]
        tipo_moto=request.POST["tipovehiculo"]
        marca=request.POST["marca"]
        estado=request.POST["estado"]
        modelo=request.POST["modelo"]
        color=request.POST["color"]
        anno=request.POST["anno"]
        file=request.POST["file"]
        comentario=request.POST["comentario"]

        objtipo=tipo_vehiculo.objects.get(idtipo=tipo_moto)
        obj=Auto.objects.create( PatenteMoto=patente,
                                 idtipo=objtipo,
                                 marca=marca,
                                 estado=estado,
                                 modelo=modelo,
                                 color=color,
                                 anno=anno,
                                 file=file,
                                 comentario=comentario)
        obj.save()
        context={'mensaje':"Datos guardados"}
        return render(request, 'core/añadirmoto.html',context)
def borrar_moto(request,pk):
    context={}
    try:
        moto=Motocicleta.objects.get(PatenteMoto=pk)
        moto.delete()
        mensaje="Datos eliminados"
        motos=Motocicleta.objects.all()
        context={'motos': motos, "mensaje": mensaje}
        return render(request, 'core/lista_moto.html', context)
    except:
        mensaje="Error, patente no existe"
        autos=Auto.objects.all()
        context={'autos':autos,'mensaje':mensaje}
        return render(request,'core/lista_moto.html', context)

def modificar_moto(request,pk):
    if pk !="":
        moto=Motocicleta.objects.get(PatenteMoto=pk)
        tpmoto=tipo_vehiculo.objects.all()

        print(type(moto.idtipo.nombre_vehiculo))

        context={'moto':moto, 'tpmoto':tpmoto}
        if moto:
            return render(request,'editar_moto',context)
        else:
            context={'mensaje':"Error, patente no existe"}
            return render(request, 'lista_moto.html',context)

def motoUpdate(request):
    if request.method == "POST":
        patente=request.POST["patente"]
        tipo_auto=request.POST["tipovehiculo"]
        marca=request.POST["marca"]
        estado=request.POST["estado"]
        modelo=request.POST["modelo"]
        color=request.POST["color"]
        anno=request.POST["anno"]
        file=request.POST["file"]
        comentario=request.POST["comentario"]

        objtipo=tipo_vehiculo.objects.get(idtipo =tipo_auto)

        moto=Motocicleta()
        moto.PatenteMoto=patente
        moto.idtipo=objtipo
        moto.marca=marca
        moto.estado=estado
        moto.modelo=modelo
        moto.color=color
        moto.anno=anno
        moto.file=file
        moto.comentario=comentario
        moto.save()

        tipo=tipo_vehiculo.objects.all()
        context={'mensaje':"Datos actualizados",'tipo':tipo,'moto':moto }
        return render(request, 'core/editar_moto.html', context)
    else:
        motos=moto.objects.all()
        context={'motos':motos}
        return render(request, 'core/lista_moto.html', context)
    
'''@csrf_exempt
@api_view(['GET','POST'])
#sacarlo del comentario cuando se ingresen valores
#@permission_classes((IsAuthenticated,))
def lista_auto(request):
    if request.method == 'GET':
        query=Auto.objects.all()
        serializer=AutoSerializer(query)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=AutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_autos(request,id):
    try:
        autos= Auto.objects.get(modelo=id)
    except Auto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer= AutoSerializer(autos)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = AutoSerializer(autos,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)  
    if request.method == 'DELETE':
        autos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        
    
    
@csrf_exempt
@api_view(['GET','POST'])
#sacarlo del comentario cuando se ingresen valores
#@permission_classes((IsAuthenticated,))
def lista_motos(request):
    if request.method == 'GET':
        query=Motocicleta.objects.all()
        serializer=MotocicletaSerializer(query, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=MotocicletaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
#@permission_classes((IsAuthenticated,))
def detalle_motos(request,id):
    try:
        motos= Motocicleta.objects.get(modelo=id)
    except Motocicleta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer= MotocicletaSerializer(motos)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer= MotocicletaSerializer(motos,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_204_NO_CONTENT)'''

#Intento de api