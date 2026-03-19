# TodoApp

`TodoApp` es un proyecto de FastAPI para gestionar tareas pendientes con persistencia en base de datos.

## Qué hace este proyecto

La aplicación permite:

- listar todas las tareas
- obtener una tarea por `id`
- crear nuevas tareas
- actualizar tareas existentes
- eliminar tareas

A diferencia de `Project1`, este proyecto no trabaja solo en memoria. Usa `SQLAlchemy` con una base de datos `SQLite`, por lo que los datos se guardan en el archivo local `todos.db`.

## Archivos principales

### `main.py`
Contiene la aplicación FastAPI, la definición de endpoints y la lógica para conectarse a la base de datos mediante dependencias.

### `models.py`
Define el modelo `Todos` con SQLAlchemy. La tabla incluye:

- `id`
- `title`
- `description`
- `priority`
- `complete`

### `database.py`
Configura la conexión a SQLite, el `engine`, la sesión (`SessionLocal`) y la clase base para los modelos.

## Requisitos

Instala las dependencias desde esta carpeta:

```bash
pip install -r requirements.txt
```

## Cómo ejecutar

Desde la carpeta `TodoApp`, corre:

```bash
uvicorn main:app --reload
```

## Endpoints principales

- `GET /todos/` devuelve todas las tareas
- `GET /todos/{todo_id}` devuelve una tarea por `id`
- `POST /todos/` crea una tarea
- `PUT /todos/{todo_id}` actualiza una tarea existente
- `DELETE /todos/{todo_id}` elimina una tarea

## Validaciones del modelo de entrada

El modelo `TodoRequest` valida lo siguiente:

- `title` debe tener al menos 3 caracteres
- `description` tiene un máximo de 100 caracteres
- `priority` debe estar entre 1 y 5
- `complete` debe ser un valor booleano

## Ejemplo de creación

```json
{
  "title": "Estudiar FastAPI",
  "description": "Repasar rutas, modelos y base de datos",
  "priority": 3,
  "complete": false
}
```

## Documentación interactiva

Con la aplicación corriendo, puedes abrir:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Nota

La tabla se crea automáticamente al iniciar la aplicación si no existe. La base de datos se guarda localmente como `todos.db` dentro del proyecto.
