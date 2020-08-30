"""Layout views."""

# Django REST Framework
from rest_framework import status, viewsets

# Serializers
from eventup.event_templates.serializers import TemplateCreateSerializer


from eventup.utils.interface.responses import CustomActions


class TemplateViewSet(viewsets.GenericViewSet):
    """ Template view set

        Crud for templates
     """

    def create(self, request, *args, **kwargs):
        """ Handle HTTP POST request """

        status_custom = False
        message = 'Error to create a new Template'
        serializer = TemplateCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        template = serializer.save()

        if template:
            status_custom = True
            message = "Template created with success"

        return CustomActions().custom_response(status.HTTP_200_OK, status_custom, message)