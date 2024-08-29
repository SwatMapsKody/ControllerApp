from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Manufacturer, Controller, Version, SupportWorkflow

# View for rendering the initial landing page
def landing_page(request):
    """
    Handles the initial loading of the landing page.
    Retrieves all manufacturers to be displayed as the first column.
    """
    manufacturers = Manufacturer.objects.all()  # Fetch all manufacturers
    return render(request, 'landing_page.html', {
        'manufacturers': manufacturers,  # Pass manufacturers to the template
    })

# View for handling manufacturer selection
def load_controllers(request, manufacturer_id):
    """
    Handles loading controllers when a manufacturer is selected.
    Fetches controllers associated with the selected manufacturer.
    Renders a partial template with the controllers.
    """
    manufacturer = get_object_or_404(Manufacturer, id=manufacturer_id)
    controllers = manufacturer.controllers.all()
    return render(request, 'partials/controllers.html', {
        'controllers': controllers,
        'manufacturer': manufacturer
    })

# View for handling controller selection
def load_versions(request, controller_id):
    """
    Handles loading versions when a controller is selected.
    Fetches versions associated with the selected controller.
    Renders a partial template with the versions.
    """
    controller = get_object_or_404(Controller, id=controller_id)
    versions = controller.versions.all()
    return render(request, 'partials/versions.html', {
        'versions': versions,
        'controller': controller
    })

# View for handling version selection
def load_workflows(request, version_id):
    """
    Handles loading workflows when a version is selected.
    Fetches workflows associated with the selected version.
    Renders a partial template with the workflows.
    """
    version = get_object_or_404(Version, id=version_id)
    workflows = version.support_workflows.all()
    return render(request, 'partials/workflows.html', {
        'workflows': workflows,
        'version': version
    })
