from django.contrib import admin
from django.urls import path, include
from ControllerSupportBot import views  # Import views module from the app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('', views.landing_page, name='landing_page'),
    path('troubleshooting/', views.troubleshooting, name='troubleshooting'),
    path('tinymce/', include('tinymce.urls')),
    path('', include('ControllerSupportBot.urls')),  # Include app-specific URLs
]