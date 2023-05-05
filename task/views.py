from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.db import IntegrityError

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm,  # envia un formulario por defecto de django
            'error': 'El usuario ya existe'
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # registrar usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()  # lo guarda en la base de datos
                login(request, user) # ? crea una cookie con los datos del usuario
                return redirect('task') # ? redirecciona al nomre de la ruta que se le diga
            except  IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,  # envia un formulario por defecto de django
                    'error': 'Usuario ya existe'
                })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,  # envia un formulario por defecto de django
                'error': 'Contraseñas no coinciden'
            })


def task(request):
    return render(request, 'task.html')

def signout(request):
    logout(request)
    return redirect('home')