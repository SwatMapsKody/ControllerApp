from django.urls import path, include
from . import views  # Import views module from the same app

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('tinymce/', include('tinymce.urls')),  # TinyMCE URLs
]
