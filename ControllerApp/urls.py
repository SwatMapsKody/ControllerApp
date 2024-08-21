"""
URL configuration for ControllerApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from ControllerSupportBot import views  # Import the entire views module

urlpatterns = [
    path('', include('ControllerSupportBot.urls')),
    path('', views.landing_page, name='landing_page'),
    path('add_controller_manufacturer/', views.add_controller_manufacturer, name='add_controller_manufacturer'),
    path('add_controller/', views.add_controller, name='add_controller'),
    path('add_support_workflow/', views.add_support_workflow, name='add_support_workflow'),
    path('view_database/', views.view_database, name='view_database'),
    path('troubleshooting/', views.troubleshooting, name='troubleshooting'),
    path('tinymce/', include('tinymce.urls'))
]
