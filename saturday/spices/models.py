from django.db import models

# Create your models here.

class SpiceMixes(models.Model):
    spice_mix_name = models.CharField(max_length=200)
    spices_id = models.ManyToManyField('Spice')


class Spice(models.Model):
    spice_mix = models.ManyToManyField('SpiceMixes')
    spice_name = models.CharField(max_length=200)
    spice_flavour_profile = models.CharField(max_length=200)