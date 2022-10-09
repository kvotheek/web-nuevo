"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    # Se incluyen las aplicaciones como parte de la ruta. De esta forma se redirigen a los archivos urls.py de cada aplicacion
    # que es lo que finalmente se modifica

    path('', include('home.urls')),  #se incluye la ruta del home, por tanto será la página principal a ver, por eso se deja en blanco.

    path('Cuestionario/', include('Cuestionario.urls')),
    path('Terminos/', include('Terminos.urls')),
    path('Test/', include('Test.urls'))



]

# Se incluye este codigo para que busque las imagenes.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)