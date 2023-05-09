from django.forms import ModelForm
from .models import Task


# ? Clase padre para tener estructuras para los formularios segun las tablas del modelo
class TaskForm(ModelForm):
    class Meta:
        # ? modelo a utilizar para el formulario
        model = Task
        # ? campos para el formulario
        fields = ["title", "description", "important"]
