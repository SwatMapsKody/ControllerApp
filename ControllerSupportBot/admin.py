from django.contrib import admin
from .models import Manufacturer, Controller, SupportWorkflow
from tinymce.widgets import TinyMCE
from django.db import models

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Fields to display in the list view
    search_fields = ('name',)  # Fields to search

class ControllerAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'model')  # Fields to display in the list view
    search_fields = ('manufacturer__name', 'model')  # Fields to search

class SupportWorkflowAdmin(admin.ModelAdmin):
    list_display = ('id', 'controller', 'question', 'answer')  # Fields to display in the list view
    search_fields = ('controller__model', 'question')  # Fields to search
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},  # Use TinyMCE for HTMLField in admin
    }

admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Controller, ControllerAdmin)
admin.site.register(SupportWorkflow, SupportWorkflowAdmin)
