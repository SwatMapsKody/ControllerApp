from django.db import models

# Create your models here.
from django.contrib import admin
from .models import MyModel
from tinymce.widgets import TinyMCE

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(MyModel, MyModelAdmin)