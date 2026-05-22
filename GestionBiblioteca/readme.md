# Gestión de préstamos de biblioteca

Este programa permite gestionar los préstamos de libros de una biblioteca desde un menú en consola.

## Funciones del programa

- Añadir un nuevo préstamo.
- Cancelar un préstamo existente.
- Listar los préstamos actuales.
- Salir del programa.

## Estructura de datos

Los préstamos se guardan en un diccionario llamado `prestamos`.

Las claves son los nombres de los lectores y los valores son listas con los libros prestados.

## Estructura del proyecto

```bash
gestion_biblioteca/
│
├── gestion_biblioteca.py
├── README.md
└── CONTRIBUTORS.md
```

## Control de errores

El programa usa excepciones personalizadas:

- `LectorNoRegistrado`: cuando el lector no existe.
- `LibroNoPrestado`: cuando el libro no está prestado a ese lector.

También controla errores como opciones no válidas o títulos vacíos.

## Ejecución

Para ejecutar el programa:

```bash
python gestion_biblioteca.py
```
