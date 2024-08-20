from django.db import models

# Create your models here.
from django.contrib import admin
from .models import MyModel
from tinymce.widgets import TinyMCE

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

class ControllerManufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Controller(models.Model):
    manufacturer = models.ForeignKey(ControllerManufacturer, on_delete=models.CASCADE, related_name='controllers')
    model = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.manufacturer.name} - {self.model}"

class SupportWorkflow(models.Model):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name='support_workflows')
    question = models.CharField(max_length=255)
    answer = RichTextField()  # Changed to RichTextField

    def __str__(self):
        return f"{self.controller.model} - {self.question}"

admin.site.register(MyModel, MyModelAdmin)