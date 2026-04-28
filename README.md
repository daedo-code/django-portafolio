# Django Portafolio

Portafolio personal desarrollado con Django, con formulario de contacto publico y panel basico para gestionar mensajes recibidos.

## Caracteristicas

- Pagina principal tipo portafolio (`/`)
- Formulario de contacto persistido en base de datos
- Pagina de agradecimiento tras envio (`/gracias/`)
- Inicio/cierre de sesion para administracion basica (`/signin/`, `/signout/`)
- Vista protegida para listar mensajes (`/mensajes/`)

## Tecnologias

- Python
- Django 5.2.6
- MySQL (driver `mysqlclient`)
- `django-environ` para variables de entorno

## Estructura del proyecto

- `core/`: configuracion principal del proyecto Django
- `mensajes/`: app de negocio (modelo, vistas, formularios, templates y estaticos)
- `manage.py`: comando principal de Django
- `.env.example`: ejemplo de variables de entorno
- `requirements.txt`: dependencias de Python

## Requisitos previos

- Python 3.11+ (recomendado)
- MySQL en ejecucion
- `pip` actualizado

## Instalacion

1. Clonar repositorio:
   ```bash
   git clone <tu-url-del-repo>
   cd django-portafolio
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\Activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Crear archivo `.env` a partir de `.env.example` y ajustar valores reales:
   ```env
   DEBUG=1
   SECRET_KEY=tu_clave_secreta
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

   DJANGO_LANGUAGE_CODE=es-es
   DJANGO_TIME_ZONE=America/Santiago

   DATABASE_NAME=tu_bd
   DATABASE_USER=tu_usuario
   DATABASE_PASSWORD=tu_password
   DATABASE_HOST=localhost
   DATABASE_PORT=3306
   ```

> Nota: este proyecto usa backend MySQL (`django.db.backends.mysql`).

5. Ejecutar migraciones:
   ```bash
   python manage.py migrate
   ```

6. Crear superusuario (opcional, recomendado):
   ```bash
   python manage.py createsuperuser
   ```

7. Levantar servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Rutas principales

- `/` -> Portafolio + formulario de contacto
- `/gracias/` -> Confirmacion de envio
- `/signin/` -> Inicio de sesion
- `/signout/` -> Cierre de sesion
- `/mensajes/` -> Listado de mensajes (requiere autenticacion)
- `/admin/` -> Panel de administracion Django

## Variables de entorno

- `DEBUG`
- `SECRET_KEY`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_LANGUAGE_CODE`
- `DJANGO_TIME_ZONE`
- `DATABASE_NAME`
- `DATABASE_USER`
- `DATABASE_PASSWORD`
- `DATABASE_HOST`
- `DATABASE_PORT`

## Licencia

Uso personal / educativo (ajustar segun tu preferencia).
