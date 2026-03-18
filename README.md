# Internaciones App

Aplicación web desarrollada con Flask que consume una API de internaciones hospitalarias y muestra los datos en una tabla paginada.

## Funcionalidades

- Listado de internaciones con paginación (20 registros por página)
- Búsqueda en tiempo real dentro de la página actual
- Cache en memoria con expiración cada 5 minutos
- Botón para forzar actualización de datos desde la API
- Badges visuales por tipo de planta (UTI, NEO, otras)

## Requisitos

- Python 3.x
- Las dependencias listadas en `requirements.txt`

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/jporona/internaciones-app.git
cd internaciones-app

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la app
python3 app.py
```

Luego abrí el navegador en `http://localhost:5000`.

## Estructura

```
internaciones-app/
├── app.py                  # Aplicación Flask
├── templates/
│   └── index.html          # Template HTML
├── requirements.txt
└── README.md
```

## API

La app consume el endpoint:

```
GET http://10.0.0.71:60000/api/smc/internaciones
```

Para cambiar la URL de la API, modificá la variable `API_URL` en `app.py`.
