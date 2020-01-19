import uuid
from django.db import models
from scraping.models import City, Speciality


class Subscriber(models.Model):
    email = models.CharField(max_length=100, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.email}'
