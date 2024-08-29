from django.contrib import admin
from django.urls import path, include
from ControllerSupportBot.views import landing_page, load_controllers, load_versions, load_workflows
from ControllerSupportBot.admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),  # Use the custom admin site
    path('tinymce/', include('tinymce.urls')),  # TinyMCE URLs
    path('', include('ControllerSupportBot.urls')),  # Include other app-specific URLs
    path('', landing_page, name='landing_page'),
    path('controllers/<int:manufacturer_id>/', load_controllers, name='load_controllers'),
    path('versions/<int:controller_id>/', load_versions, name='load_versions'),
    path('workflows/<int:version_id>/', load_workflows, name='load_workflows'),
]
