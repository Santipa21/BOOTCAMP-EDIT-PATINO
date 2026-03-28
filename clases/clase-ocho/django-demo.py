import os
import sys
import django
from django.conf import settings
from django.urls import path
from django.http import HttpResponse
from django.core.management import execute_from_command_line

# ---------------------------------------------------------
# 1. CONFIGURACIÓN MÍNIMA DE DJANGO (SIN BASE DE DATOS)
# ---------------------------------------------------------

settings.configure(
    DEBUG=True,
    SECRET_KEY='clave-secreta-para-demo',
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[],  # ⬅️ Sin apps, sin base de datos
    MIDDLEWARE=[
        'django.middleware.security.SecurityMiddleware',
        'django.middleware.common.CommonMiddleware',
    ],
    ALLOWED_HOSTS=['*'],
)

# ---------------------------------------------------------
# 2. VISTAS
# ---------------------------------------------------------

def home_view(request):
    content = """
    <html>
        <head>
            <title>Django Demo</title>
            <style>
                body { font-family: sans-serif; text-align: center; padding: 50px; background-color: #f0f0f0; }
                h1 { color: #0c4b33; }
                .box { background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
                code { background: #eee; padding: 2px 5px; border-radius: 3px; }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>¡Hola Mundo desde Django!</h1>
                <p>Este proyecto se ejecuta desde un único archivo: <code>django-demo.py</code></p>
                <p>Estado del servidor: <strong>Activo</strong> ✅</p>
                <p><em>Sin base de datos configurada</em></p>
                <hr>
                <p>Prueba la otra ruta: <a href="/about">/about</a></p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(content)

def about_view(request):
    return HttpResponse("<h1>Página 'Sobre Nosotros'</h1><p>Esta es una ruta secundaria.</p><a href='/'>Volver al inicio</a>")

# ---------------------------------------------------------
# 3. URLS
# ---------------------------------------------------------

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
]

# ---------------------------------------------------------
# 4. EJECUCIÓN
# ---------------------------------------------------------

if __name__ == '__main__':
    django.setup()
    sys.argv = ['django-demo.py', 'runserver', '127.0.0.1:8000']
    execute_from_command_line(sys.argv)