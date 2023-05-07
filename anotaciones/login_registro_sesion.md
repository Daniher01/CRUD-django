# Anotaciones

### Crear cookies de sesion
```python
    #primero importar
    from django.contrib.auth import login

    #creando la cookie
    login(request, user)
```

### Cerrar sesion y elimina cookie
```python
    #primero importar
    from django.contrib.auth import logout

    #eliminando la cookie
    logout(request, user)
```

### Registrar usuario
Se puede registrar un usuario con un formulario ya reado de django, solo hay que importar la librería
```python
    #primero importar
    from django.contrib.auth.forms import UserCreationForm

    #enviando el formulario a la vista
    render(
        request,
        'signup.html', {
        'form': UserCreationForm 
    })
```

### Iniciar sesion de usuario
Se puede iniciar la sesion de un usuario con un formulario ya reado de django, solo hay que importar la librería
```python
    #primero importar
    from django.contrib.auth.forms import AuthenticationForm

    #enviando el formulario a la vista
    render(
        request,
        'signin.html', {
        'form': AuthenticationForm 
    })
```

- **Autenticar el usuario:**
Existe uan libreria que te permite autenticar el usuario
 ```python
    #primero importar
    from django.contrib.auth import authenticate

    #comprobar el usuario y la contraseña
    # retorna un usuario si esta autenticado
    # retorna nulo o none si no esta autenticado
    user = authenticate(
        request,
        username=request.POST["username"],
        password=request.POST["password"],
    )
```      