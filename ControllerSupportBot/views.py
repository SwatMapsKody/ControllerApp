from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Manufacturer, Controller, Version, SupportWorkflow

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



def get_controllers(request, manufacturer_id):
    manufacturer = get_object_or_404(Manufacturer, id=manufacturer_id)
    controllers = list(manufacturer.controllers.all().values('id', 'model'))
    return JsonResponse(controllers, safe=False)

def get_versions(request, controller_id):
    controller = get_object_or_404(Controller, id=controller_id)
    versions = list(controller.versions.all().values('id', 'version'))
    return JsonResponse(versions, safe=False)

def get_workflows(request, version_id):
    version = get_object_or_404(Version, id=version_id)
    workflows = list(version.support_workflows.all().values('id', 'question', 'answer'))
    return JsonResponse(workflows, safe=False)
