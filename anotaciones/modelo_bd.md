# Anotaciones 

### Crear un modelo de la tabla
crea la estructura y los atributos de la tabla

- En la carpeta del la app _en este caso task_, en el archivo **models.py**
``` python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  created = models.DateTimeField(auto_now_add=True)
  datecompleted = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
      return self.title
```
- **Ejecutar cada vez que se cree una tabla**
``` shell
    python manage.py makemigrations # crea una migracion
    python manage.py migrate # registra el cambio
```

### Crear tabla
crea la tabla en la base de datos

**Requisito:** Tener acceso al panel de administracion

- Dentro de _task_ en el archivo **admin.py**
``` python
    from django.contrib import admin
    from .models import Task

    # Register your models here.
    admin.site.register(Task) # crea la tabla Task
```