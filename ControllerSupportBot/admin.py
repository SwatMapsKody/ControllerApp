from django.contrib import admin
from .models import Manufacturer, Controller, Version, SupportWorkflow
from tinymce.widgets import TinyMCE
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomAdminSite(admin.AdminSite):
    site_header = "Controller App Admin"
    site_title = "Controller App Admin Portal"
    index_title = "Welcome to the Controller App Admin Portal"

    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        for app_name, app in app_dict.items():
            if app_name == "ControllerSupportBot":
                app['models'].sort(key=lambda x: {
                    'Manufacturers': 0,
                    'Controllers': 1,
                    'Versions': 2,
                    'Support Workflows': 3
                }.get(x['name'], 100))
        return sorted(app_dict.values(), key=lambda x: x['name'].lower())

custom_admin_site = CustomAdminSite(name='custom_admin')

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class ControllerAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'model')
    search_fields = ('manufacturer__name', 'model')

class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'controller', 'version')
    search_fields = ('controller__model', 'version')

class SupportWorkflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'version', 'question', 'answer')
    search_fields = ('version__controller__model', 'version__version', 'question')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

custom_admin_site.register(Manufacturer, ManufacturerAdmin)
custom_admin_site.register(Controller, ControllerAdmin)
custom_admin_site.register(Version, VersionAdmin)
custom_admin_site.register(SupportWorkflow, SupportWorkflowAdmin)
