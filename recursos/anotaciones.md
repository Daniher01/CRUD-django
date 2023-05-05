# Anotaciones del tutorial

#### Project Setup

- activar entorno virtual
- instalar django
- iniciar proyecto
    ``` shell
        django-admin startproject nombre_proyecto . 
        #el . para que lo inizalice en la misma carpeta
    ```
- correr el servidor   
    ``` shell
        python manage.py runserver
    ```
- iniciar una App
    ``` shell
        python manage.py startapp nombre_app
    ```        

### Crear las tablas
``` shell
    python manage.py migrate 
```

### Crear cookies de sesion
```shell
    #primero importar
    from django.contrib.auth import login

    #creando la cookie
    login(request, user)
```

### Cerrar sesion y elimina cookie
```shell
    #primero importar
    from django.contrib.auth import logout

    #eliminando la cookie
    logout(request, user)
```


        