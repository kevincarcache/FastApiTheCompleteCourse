# FastApiTheCompleteCourse

Repositorio de práctica para aprender Python y FastAPI siguiendo un curso. Aquí se combinan ejercicios básicos del lenguaje con varios proyectos de API usando FastAPI.

## Contenido del repositorio

### `introduction/`
Contiene ejercicios introductorios de Python para reforzar fundamentos como:

- variables y comentarios
- strings y formateo
- listas, sets, tuplas y diccionarios
- condicionales y loops
- funciones e imports
- programación orientada a objetos

Estos archivos están pensados como ejemplos pequeños y ejercicios independientes.

### `Project1/`
Incluye un proyecto inicial con FastAPI orientado a la gestión de libros. En esta carpeta hay dos versiones de la API:

- `books.py`: versión sencilla con una lista en memoria y endpoints básicos usando libros reales de autoayuda.
- `books2.py`: versión más completa con validación usando `Pydantic`, asignación automática de `id` y operaciones CRUD sobre una colección de 10 libros de autoayuda.

También incluye un archivo `requirements.txt` con las dependencias necesarias para ejecutar la API.

### `TodoApp/`
Incluye un segundo proyecto con FastAPI para administrar tareas pendientes.

- usa `SQLAlchemy` para persistir los datos
- utiliza una base de datos `SQLite` local (`todos.db`)
- expone endpoints CRUD para crear, consultar, actualizar y eliminar tareas
- valida la entrada con `Pydantic`

## Tecnologías usadas

- Python
- FastAPI
- Pydantic
- Uvicorn
- SQLAlchemy
- SQLite

## Cómo ejecutar los proyectos

### `Project1`

1. Entrar a la carpeta del proyecto:

```bash
cd Project1
```

2. Crear y activar un entorno virtual si se desea:

```bash
python -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Levantar la API:

```bash
uvicorn books:app --reload
```

O, si quieres probar la segunda versión:

```bash
uvicorn books2:app --reload
```

### `TodoApp`

1. Entrar a la carpeta del proyecto:

```bash
cd TodoApp
```

2. Crear y activar un entorno virtual si se desea:

```bash
python -m venv venv
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Levantar la API:

```bash
uvicorn main:app --reload
```

## Documentación automática

Una vez ejecutada la aplicación, FastAPI genera documentación interactiva en:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Objetivo del repositorio

Este repositorio funciona como base de aprendizaje. Primero se practican los fundamentos de Python y luego se aplican esos conocimientos en proyectos de API con FastAPI.

Actualmente, el repositorio incluye un proyecto de libros en memoria y otro de tareas con persistencia en base de datos, lo que permite practicar distintos niveles de complejidad dentro de FastAPI.
