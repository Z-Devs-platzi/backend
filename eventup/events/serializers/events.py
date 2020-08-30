""" Events Serializer """

# Django REST Framework
from rest_framework import serializers

# Models
from eventup.events.models import Event


class EventModelSerializer(serializers.ModelSerializer):
    """ Event model serializer """

    class Meta:
        """ Meta class """

        model = Event
        fields = (
            'name',
            'data',
            'description',
            'url',
            'banner_img',
            'banner_title',
            'template',
            'sponsor',
            'schedule',
        )


class EventCreateSerializer(serializers.Serializer):
    """ Event create serializer """

    name = serializers.CharField()

    def create(self, data):
        event = Event.objects.create(**data)

        return event
