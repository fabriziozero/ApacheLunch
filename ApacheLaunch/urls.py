"""ApacheLaunch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
<<<<<<< HEAD

from ApacheLaunch.views import saludo, despedida, dameFecha, calculaEdad

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/',admin.site.urls),
<<<<<<< HEAD
=======
from ApacheLaunch.views import saludo, despedida, dameFecha, calculaEdad

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('mano/', saludo),
    path('pie/', despedida),
    path('fecha/', dameFecha),
    path('edades/<int:edad>/<int:anho>', calculaEdad)
>>>>>>> c043b222d1f42fa89e2d83d879d6fcdfcbaa7f2e
=======
    path('saludo/', saludo),
    path('mano/', despedida),
    path('fecha/', dameFecha),
    path('edad/<int:edad>/<int:anho>/', calculaEdad)
>>>>>>> miguel
]

