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
        fields = ['manufacturer', 'model']

class SupportWorkflowForm(forms.ModelForm):
    class Meta:
        model = SupportWorkflow
        fields = ['controller', 'question', 'answer']
        widgets = {
            'controller': forms.Select(choices=[(c.id, str(c)) for c in Controller.objects.all()]),  # Dropdown for controllers
            'question': forms.TextInput(attrs={'placeholder': 'Enter your question here', 'class': 'form-control'}),
            'answer': TinyMCE(attrs={'cols': 80, 'rows': 30}),  # Rich text editor for answer
        }