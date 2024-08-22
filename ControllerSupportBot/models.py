from django.db import models
from tinymce.models import HTMLField  # Assuming you're still using TinyMCE for HTML content

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Controller(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='controllers')
    model = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.manufacturer.name} - {self.model}"

class Version(models.Model):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name='versions')
    version = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.controller.model} - {self.version}"

class SupportWorkflow(models.Model):
    version = models.ForeignKey(Version, on_delete=models.CASCADE, related_name='support_workflows')
    question = models.CharField(max_length=255)
    answer = HTMLField()

    def __str__(self):
        return f"{self.version.controller.model} - {self.question} - {self.answer}"
