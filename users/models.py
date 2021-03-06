from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from data.models import Project, Cause


class Donor(models.Model):
    donor_id = models.ForeignKey(User, on_delete=models.SET('team member not set'))
    name = models.CharField(max_length=128, blank=False,)
    mobile = models.BigIntegerField(null = True)
    email = models.EmailField(max_length = 254)
    transaction_id = models.BigIntegerField(null = False)
    project = models.ForeignKey(Project, on_delete=models.SET('project not set'), default=2333)

    def __unicode__(self):
        return self.name


class Donation(models.Model):
    name = models.CharField(default='not set', max_length=150)
    transaction_id = models.CharField(default='not set', max_length=150, primary_key=True)
    donor_id = models.ForeignKey(User, on_delete=models.SET('team member not set'))
    project_id = models.ForeignKey(Project, on_delete=models.SET('project not set'))
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
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
    pincode = models.IntegerField(default=0)

    def __int__(self):
        return self.username.first_name + "" + self.username.last_name


class Notification(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET('team member not set'))
    supported_projects_mobile = models.BooleanField(default=True)
    supported_projects_email = models.BooleanField(default=True)
    general_mobile = models.BooleanField(default=True)
    general_email = models.BooleanField(default=True)
    exciting_projects_mobile = models.BooleanField(default=True)
    exciting_projects_email = models.BooleanField(default=True)


class Card_Details(models.Model):
    username = models.ForeignKey(User, on_delete=models.SET('team member not set'))
    card_number = models.BigIntegerField()
    card_holder =  models.CharField(max_length=40, default="", blank=True)
    expiration_date = models.CharField(max_length=40)
    cvv = models.IntegerField()

class Causes_I_Care_About(models.Model):
    primary_key = models.CharField(primary_key=True, max_length=150, default='not set')
    username = models.ForeignKey(User, on_delete=models.SET('team member not set'))
    cause = models.ForeignKey(Cause)

