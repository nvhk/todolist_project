"""todolist URL Configuration

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
from django.urls import path
from todo import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('rejestracja/', views.rejestracja, name='rejestracja'),
    path('wyloguj/', views.wyloguj, name='wyloguj'), 
    path('zaloguj/', views.zaloguj, name='zaloguj'),

    # Todos
    path('todosy/', views.todosy, name='todosy'),
    path('', views.home, name='home'),
    path('dodaj/', views.dodaj, name='dodaj'),
    path('zrobione/', views.zrobione, name='zrobione'),
    path('todosy/<int:todosy_pk>', views.zobacztodos, name='zobacztodos'),
    path('todosy/<int:todosy_pk>/wykonanie', views.wykonanie, name='wykonanie'),
    path('todosy/<int:todosy_pk>/usun', views.usun, name='usun'),
]