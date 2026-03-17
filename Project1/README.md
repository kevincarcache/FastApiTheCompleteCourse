# Project1

`Project1` es un proyecto introductorio de FastAPI enfocado en crear una API simple para gestionar libros en memoria.

La temática actual del proyecto usa libros reales de autoayuda y desarrollo personal para hacer los ejemplos más cercanos a un caso real.

## Archivos principales

### `books.py`
Versión básica de la API. Incluye endpoints para:

- obtener todos los libros
- buscar un libro por título
- filtrar libros por categoría
- crear un nuevo libro

Usa una lista de diccionarios como almacenamiento temporal, por lo que los datos se pierden al reiniciar la aplicación. La lista inicial incluye títulos populares como `Atomic Habits`, `The 5 Second Rule` y `The Mountain Is You`.

### `books2.py`
Versión más completa del ejemplo. Mantiene los libros en memoria, pero ahora incluye:

- validación de datos con `Pydantic` y `Field`
- asignación automática del `id` al crear un libro
- búsqueda por `id`
- filtro por `rating`
- creación, actualización y eliminación de libros

La colección inicial contiene 10 libros reales de autoayuda.

## Requisitos

Instala las dependencias desde esta carpeta:

```bash
pip install -r requirements.txt
```

## Cómo ejecutar

Para correr la primera versión:

```bash
uvicorn books:app --reload
```

Para correr la segunda versión:

```bash
uvicorn books2:app --reload
```

## Endpoints principales

### En `books.py`

- `GET /books` devuelve todos los libros
- `GET /books/{book_title}` busca un libro por título
- `GET /books/?category=self-help` filtra por categoría
- `POST /books/create_book` agrega un libro nuevo

Ejemplo de cuerpo para crear un libro:

```json
{
  "title": "The Power of Habit",
  "author": "Charles Duhigg",
  "category": "self-help"
}
```

### En `books2.py`

- `GET /books` devuelve todos los libros
- `GET /books/{book_id}` busca un libro por `id`
- `GET /books/?rating=5` filtra por calificación
- `POST /books` crea un libro nuevo y asigna el `id` automáticamente
- `PUT /books/{book_id}` actualiza un libro existente
- `DELETE /books/{book_id}` elimina un libro existente

Reglas de validación del modelo `BookRequest`:

- `id` es opcional al crear
- `title` debe tener al menos 3 caracteres
- `author` debe tener al menos 1 caracter
- `description` debe tener entre 1 y 100 caracteres
- `rating` debe estar entre 1 y 5

Ejemplo de cuerpo para crear un libro:

```json
{
  "title": "The Power of Habit",
  "author": "Charles Duhigg",
  "description": "A book about the science of habit formation and how to change habits.",
  "rating": 5
}
```

Ejemplo de cuerpo para actualizar un libro:

```json
{
  "title": "Deep Work",
  "author": "Cal Newport",
  "description": "A book about focus, concentration, and meaningful productivity.",
  "rating": 5
}
```

## Documentación interactiva

Con la aplicación corriendo, puedes probar la API en:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Nota

Este proyecto es didáctico y no usa base de datos. Todo el contenido se guarda únicamente en memoria mientras la aplicación está en ejecución, así que cualquier cambio se pierde al reiniciar el servidor.
