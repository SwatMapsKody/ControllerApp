
from django.shortcuts import render

from .models import Manufacturer, Controller, SupportWorkflow

def landing_page(request):
    manufacturers = Manufacturer.objects.all()
    controllers = Controller.objects.select_related('manufacturer').all()
    controllers_by_manufacturer = {m.id: [] for m in manufacturers}
    for controller in controllers:
        controllers_by_manufacturer[controller.manufacturer.id].append(controller)

    return render(request, 'landing_page.html', {
        'manufacturers': manufacturers,
        'controllers_by_manufacturer': controllers_by_manufacturer
    })


def troubleshooting(request):
    manufacturers = Manufacturer.objects.all()
    selected_manufacturer = None
    selected_controller = None
    workflows = None

    if 'manufacturer' in request.GET:
        selected_manufacturer = Manufacturer.objects.get(id=request.GET['manufacturer'])
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
