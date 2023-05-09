from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm

# Create your views here.


def home(request):
    return render(request, "home.html")


# ? registro del usuario con UserCreationForm
def signup(request):
    if request.method == "GET":
        return render(
            request,
            "signup.html",
            {
                "form": UserCreationForm,  # envia un formulario por defecto de django
                "error": "El usuario ya existe",
            },
        )
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # registrar usuario
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()  # lo guarda en la base de datos
                login(request, user)  # ? crea una cookie con los datos del usuario
                return redirect(
                    "task"
                )  # ? redirecciona al nomre de la ruta que se le diga
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {
                        "form": UserCreationForm,  # envia un formulario por defecto de django
                        "error": "Usuario ya existe",
                    },
                )
        else:
            return render(
                request,
                "signup.html",
                {
                    "form": UserCreationForm,  # envia un formulario por defecto de django
                    "error": "Contraseñas no coinciden",
                },
            )


def task(request):
    return render(request, "task.html")


def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)  # ? crea un formulario
            new_task = form.save(
                commit=False
            )  # ? commit=False evita que lo guarde en la bd
            new_task.user = request.user
            new_task.save()
            return redirect("task")
        except ValueError:
            return render(
                request,
                "create_task.html",
                {"form": TaskForm, "error": "Datos invalidos"},
            )


def signout(request):
    logout(request)
    return redirect("home")


# ? inicio de sesion con AuthenticationForm
def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm,
                    "error": "Username or password is incorrect",
                },
            )
        else:
            login(request, user)
            return redirect("task")
