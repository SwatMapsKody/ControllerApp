from django.contrib import admin
from .models import ControllerManufacturer, Controller, SupportWorkflow
from tinymce.widgets import TinyMCE
from django.db import models

class ControllerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(ControllerManufacturer)
admin.site.register(Controller, ControllerAdmin)
admin.site.register(SupportWorkflow, ControllerAdmin)