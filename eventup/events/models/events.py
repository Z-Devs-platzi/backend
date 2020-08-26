''' Events Model '''

import uuid
from django.db import models

# Utils Model
from eventup.utils.models import GeneralModel


class Event(GeneralModel):
    ''' Event Model '''
    # Id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Event data
    name = models.CharField(max_length=100, unique=True)
    date = models.DateField()
    hour = models.TimeField()
    description = models.TextField()
    url = models.URLField()
    banner = models.URLField()
    logo = models.URLField()

    # Event Relations
    sponsor = models.ManyToManyField(
        to="Sponsor",
    )

    schedule = models.OneToOneField(
        to="Schedule",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return str(self.name)
