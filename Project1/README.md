# Project1

`Project1` es un proyecto introductorio de FastAPI enfocado en crear una API simple para gestionar libros en memoria.

## Archivos principales

### `books.py`
Versión básica de la API. Incluye endpoints para:

- obtener todos los libros
- buscar un libro por título
- filtrar libros por categoría
- crear un nuevo libro

Usa una lista de diccionarios como almacenamiento temporal, por lo que los datos se pierden al reiniciar la aplicación.

### `books2.py`
Versión mejorada del ejemplo. Mantiene los libros en memoria, pero usa un modelo de entrada con `Pydantic` (`BookRequest`) para validar los datos recibidos en el endpoint `POST`.

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
- `GET /books/?category=...` filtra por categoría
- `POST /books/create_book` agrega un libro nuevo

Ejemplo de cuerpo para crear un libro:

```json
{
  "title": "Nuevo Libro",
  "author": "Autor",
  "category": "science"
}
```

### En `books2.py`

- `GET /books/` devuelve todos los libros
- `POST /books/` crea un libro nuevo validado con Pydantic

Ejemplo de cuerpo para crear un libro:

```json
{
  "id": 6,
  "title": "Adicciones 6",
  "author": "Kevin Carcache",
  "description": "Excelente Libro",
  "rating": 5
}
```

## Documentación interactiva

Con la aplicación corriendo, puedes probar la API en:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Nota

Este proyecto es didáctico y no usa base de datos. Todo el contenido se guarda únicamente en memoria mientras la aplicación está en ejecución.
