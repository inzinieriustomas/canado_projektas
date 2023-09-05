"""
URL configuration for canado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from app_canado import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('car.urls')),
    path('works/', include('works.urls')),
    path('main_page/', views.main_page, name='main_page'),
    path('vadybininkui/', views.vadybininkui, name='vadybininkui'),
    path('dazytojui/', views.dazytojui, name='dazytojui'),
    path('mechanikui/', views.mechanikui, name='mechanikui'),
    path('saltkalviui/', views.saltkalviui, name='saltkalviui'),
    path('elektrikui/', views.elektrikui, name='elektrikui'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', success_url='/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html', next_page='main_page'), name='logout'),
    # path('darbuotojui/', views.darbuotojui, name='darbuotojui'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html', success_url='/works/darbuotojo_darbai/'), name='login'),


    # path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
