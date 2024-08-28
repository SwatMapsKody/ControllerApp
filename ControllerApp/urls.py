from django.contrib import admin
from django.urls import path, include
from ControllerSupportBot import views  # Import views module from the app
from ControllerSupportBot.admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),  # Use the custom admin site
    path('', views.landing_page, name='landing_page'),  # Landing page
    path('troubleshooting/', views.troubleshooting, name='troubleshooting'),  # Troubleshooting page
    path('tinymce/', include('tinymce.urls')),  # TinyMCE URLs
    path('', include('ControllerSupportBot.urls')),  # Include other app-specific URLs
    path('controllers/<int:manufacturer_id>/', views.get_controllers, name='get_controllers'),
    path('versions/<int:controller_id>/', views.get_versions, name='get_versions'),
    path('workflows/<int:version_id>/', views.get_workflows, name='get_workflows'),
]
