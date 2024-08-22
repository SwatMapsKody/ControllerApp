from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.template.loader import render_to_string

from .models import ControllerManufacturer, Controller, SupportWorkflow
from .forms import ControllerManufacturerForm, ControllerForm, SupportWorkflowForm

def add_controller_manufacturer(request):
    if request.method == 'POST':
        form = ControllerManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_controller_manufacturer')
    else:
        form = ControllerManufacturerForm()
    return render(request, 'add_controller_manufacturer.html', {'form': form})

def add_controller(request):
    if request.method == 'POST':
        form = ControllerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_controller')
    else:
        form = ControllerForm()
    return render(request, 'add_controller.html', {'form': form})

def add_support_workflow(request):
    if request.method == 'POST':
        form = SupportWorkflowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_support_workflow')
    else:
        form = SupportWorkflowForm()
    return render(request, 'add_support_workflow.html', {'form': form})

def view_database(request):
    manufacturers = ControllerManufacturer.objects.all()
    controllers = Controller.objects.all()
    workflows = SupportWorkflow.objects.all()

    context = {
        'manufacturers': manufacturers,
        'controllers': controllers,
        'workflows': workflows,
    }

    return render(request, 'view_database.html', context)

def troubleshooting(request):
    manufacturers = ControllerManufacturer.objects.all()
    selected_manufacturer = None
    selected_controller = None
    workflows = None

    if 'manufacturer' in request.GET:
        selected_manufacturer = ControllerManufacturer.objects.get(id=request.GET['manufacturer'])
        controllers = selected_manufacturer.controllers.all()
    else:
        controllers = None

    if 'controller' in request.GET and controllers:
        selected_controller = Controller.objects.get(id=request.GET['controller'])
        workflows = selected_controller.support_workflows.all()

    context = {
        'manufacturers': manufacturers,
        'controllers': controllers,
        'workflows': workflows,
        'selected_manufacturer': selected_manufacturer,
        'selected_controller': selected_controller,
    }
    return render(request, 'troubleshooting.html', context)


def update_workflow_answer(request, workflow_id):
    workflow = get_object_or_404(SupportWorkflow, id=workflow_id)

    if request.method == 'POST':
        form = SupportWorkflowForm(request.POST, instance=workflow)
        if form.is_valid():
            form.save()
            return redirect('view_database')  # Redirect to the database view
    else:
        form = SupportWorkflowForm(instance=workflow)

    return render(request, 'view_database', {'form': form, 'workflow': workflow})

def landing_page(request):
    return render(request, 'landing_page.html')


def delete_entry(request, entry_id, model_type):
    if model_type == 'controller':
        entry = get_object_or_404(Controller, id=entry_id)
    elif model_type == 'manufacturer':
        entry = get_object_or_404(ControllerManufacturer, id=entry_id)
    elif model_type == 'workflow':
        entry = get_object_or_404(SupportWorkflow, id=entry_id)
    else:
        return HttpResponseNotFound("Model type not supported")

    entry.delete()
    return redirect('view_database')

def edit_entry(request, entry_id, model_name):
    if model_name == 'manufacturer':
        model = ControllerManufacturer
        form_class = ControllerManufacturerForm
    elif model_name == 'controller':
        model = Controller
        form_class = ControllerForm
    elif model_name == 'support_workflow':
        model = SupportWorkflow
        form_class = SupportWorkflowForm
    else:
        return JsonResponse({'error': 'Invalid model name'}, status=400)

    entry = get_object_or_404(model, id=entry_id)

    if request.method == 'POST':
        form = form_class(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = form_class(instance=entry)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Render the form for the modal
            html = render_to_string('edit_modal_form.html', {'form': form, 'model_name': model_name})
            return JsonResponse({'html': html})
        else:
            return render(request, 'view_database.html', {'form': form, 'model_name': model_name})


