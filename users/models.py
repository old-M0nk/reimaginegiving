from __future__ import unicode_literals

from django.db import models
from data.models import Project

class Donor(models.Model):
    donor_id = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=128, blank=False,)
    mobile = models.BigIntegerField(null = True)
    email = models.EmailField(max_length = 254)
    transaction_id = models.BigIntegerField(null = False)
    def __unicode__(self):
        return self.name

class Donation(models.Model):
    transaction_id = models.BigIntegerField(null = False)
    donor_id = models.ForeignKey('Donor', on_delete=models.SET('donor not assigned'))
    project_id = models.ForeignKey(Project, on_delete=models.SET('project not set'))
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null = False)
    time = models.TimeField(auto_now = True)
#
# class Email(models.Model):
#     email = models.EmailField(max_length=254, primary_key=True)

