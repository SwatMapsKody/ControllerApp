from django.db import models
from tinymce.models import HTMLField  # Use HTMLField for TinyMCE

class ControllerManufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Controller(models.Model):
    manufacturer = models.ForeignKey(ControllerManufacturer, on_delete=models.CASCADE, related_name='controllers')
    model = models.CharField(max_length=100)
    description = HTMLField(blank=True, null=True)  # Changed to HTMLField

    def __str__(self):
        return f"{self.manufacturer.name} - {self.model}"

class SupportWorkflow(models.Model):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name='support_workflows')
    question = models.CharField(max_length=255)
    answer = HTMLField()  # Changed to HTMLField

    def __str__(self):
        return f"{self.controller.model} - {self.question}"
