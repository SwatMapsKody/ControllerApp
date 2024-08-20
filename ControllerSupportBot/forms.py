from django import forms
from tinymce.widgets import TinyMCE
from .models import ControllerManufacturer, Controller, SupportWorkflow

class MyForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

class ControllerManufacturerForm(forms.ModelForm):
    class Meta:
        model = ControllerManufacturer
        fields = ['name']

class ControllerForm(forms.ModelForm):
    class Meta:
        model = Controller
        fields = ['manufacturer', 'model', 'description']

class SupportWorkflowForm(forms.ModelForm):
    class Meta:
        model = SupportWorkflow
        fields = ['controller', 'question', 'answer']
        widgets = {
            'answer': forms.Textarea(attrs={'class': 'ckeditor'}),  # Use CKEditor widget
        }

