# *sistema de gestion de libros*

Este proyecto es una aplicación web desarrollada con Django que permite gestionar autores y libros, esta organzanizado y divido por un *backend* y un *frontend*, utiliza SQLite.

# descripcion general:

-el sistema permite lo siguiente:

-resgitrar,eliminar y actualizar autores
-registrar,eliminar y actualizar autores
-motrar informacion de autores y libros 


# estructura del proyecto:

backend/
├── app/
│   ├── autor/
│   ├── libro/
│   ├── db.sqlite3          # Base de datos SQLite del proyecto
│   └── manage.py           # Script de gestión para la aplicación
│
├── front/
│   ├── controladores/    
│   ├── modelos/            
│   └── vistas/             # Vistas e interfaces de usuario
│
├── __main__.py             # Punto de entrada principal del proyecto
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias necesarias para el entorno
├── respaldo_autores.txt    # Respaldo de datos de autores
├── respaldo_libros.txt     # Respaldo de datos de libros


 # Instrucciones para Ejecutar el Proyecto

---

# 1. Ejecutar el Backend

Desde la carpeta `backend/`:

```bash
cd backend
```

---

Si es la **primera vez que se ejecuta** o se **hacen cambios en los modelos**, se ejecuta:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

Luego, para inicializar el servidor:

```bash
python manage.py runserver
```

---

Esto levantará la API REST en: [`http://127.0.0.1:8000/`]

---

# 2. Ejecutar la Aplicación de Escritorio (Tkinter)

Desde la carpeta `frontend/`:

```bash
cd frontend
python main.py
```

---

Esto abrirá la ventana de la aplicación de escritorio, conectada al backend vía la API REST.

---

# requisitos:

-python 3.10 o superior 

# modulos:

-*autor* = control de informacion de actores
-*libro* = registrar la informacion de libros
-- *app* = Gestión de editoriales.
-*frontend* = presenta la interfaz (controla la interfaz grafica)

# base de datos:
-se utiliza algo para recuperar datos donde se incluye `db.sqlite3`,
-para recuperar:
  - `respaldo_autores.txt`
  - `respaldo_libros.txt`

# créditos:

-Este proyecto fue desarrollado como parte del curso de desarrollo web con Django.
-Autor: [Liseth Dahiana Rengifo Poloche, Daniela Acero Betancur]
