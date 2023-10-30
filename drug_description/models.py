from django.db import models

# Models for drug descriptions DB.
class Drug(models.Model):
    name = models.CharField(max_length=255)
    medicine_id = models.IntegerField(default=000)
    is_active = models.BooleanField(default=False)
    form = models.CharField(max_length=100)
    shape = models.CharField(max_length=100, blank=True, null=True)
    colour = models.CharField(max_length=100)
    imprint = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
