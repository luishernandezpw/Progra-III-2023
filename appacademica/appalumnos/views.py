from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import alumno
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def saludo(request):
    return HttpResponse("Hola desde django")

def miEdad(request, edad):
    return HttpResponse("Hola tu edad es: %s" %edad)

def index(request):
    return render(request, 'index.html')

def alumnos(request):
    return render(request, 'alumnos.html')

@csrf_exempt
def save_alumno(request):
    datos = json.loads(request.body)
    accion = datos.get("accion")
    idA = datos.get("idAlumno")
    cod = datos.get("codigo")
    nom = datos.get("nombre")
    dir = datos.get("direccion")
    tel = datos.get("telefono")
    if accion=="nuevo":
        editAlumno = alumno.objects.create(codigo=cod, nombre=nom, direccion=dir, telefono=tel)
    elif accion=="modificar":
        editAlumno = alumno.objects.get(id=idA)
        editAlumno.codigo = cod
        editAlumno.nombre = nom
        editAlumno.direccion = dir
        editAlumno.telefono = tel
        editAlumno.save()
    elif accion=="eliminar":
        editAlumno = alumno.objects.get(id=idA)
        editAlumno.delete()
    return JsonResponse({'msg':'ok', 'idAlumno':editAlumno.id}, safe=False)

def busqueda_alumnos(request):
    return render(request, 'busqueda_alumnos.html')

@csrf_exempt
def buscar_alumnos(request):
    data = json.loads(request.body) # nombre like '%luis%'
    datos = alumno.objects.filter(nombre__icontains=data.get('buscar')).values('id', 'codigo', 'nombre', 'direccion', 'telefono')
    return JsonResponse(list(datos), safe=False)

def materias(request):
    return render(request, 'materias.html')

def busqueda_materias(request):
    return render(request, 'busqueda_materias.html')