from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from data.models import Project


class Donor(models.Model):
    donor_id = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length=128, blank=False,)
    mobile = models.BigIntegerField(null = True)
    email = models.EmailField(max_length = 254)
    transaction_id = models.BigIntegerField(null = False)
    project = models.ForeignKey(Project, on_delete=models.SET('project not set'), default=2333)

    def __unicode__(self):
        return self.name


class Donation(models.Model):
    transaction_id = models.BigIntegerField(null = False)
    donor_id = models.ForeignKey('Donor', on_delete=models.SET('donor not assigned'))
    project_id = models.ForeignKey(Project, on_delete=models.SET('project not set'))
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(null = False)
    time = models.TimeField(auto_now = True)


class Email(models.Model):
    email = models.EmailField(max_length=254, primary_key=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=254, default="blank")
    email = models.EmailField(max_length=254, blank=False)
    message = models.TextField(blank=False, default="blank")


class User_Details(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET('team member not set'))
    mobile_number = models.CharField(max_length=12, default="")
    pan_number = models.TextField(default="")
    occupation = models.TextField(default="")
    address_line_1 = models.TextField(default="")
    address_line_2 = models.TextField(default="")
    city = models.CharField(max_length=20, default="")
    pincode = models.CharField(max_length=20, default="")

    def __int__(self):
        return self.username.first_name + "" + self.username.last_name

