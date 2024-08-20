from django import forms
from .models import ControllerManufacturer, Controller, SupportWorkflow

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
