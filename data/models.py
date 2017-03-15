from __future__ import unicode_literals

from django.db import models
from staff.models import Team_Member

#KEYS NOT YET SPECIFIED
class Cause(models.Model):
    cause_id = models.CharField(max_length=10, blank=False, primary_key=True)
    name = models.CharField(max_length = 60, blank = False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "%s : %s" % (self.name, self.total_amount)

class Project(models.Model):
    project_id = models.CharField(max_length=10, blank=False, primary_key=True)
    title = models.CharField(max_length=128, blank=False,)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cause = models.ForeignKey('Cause', on_delete=models.SET('cause not set'))
    ngo_id = models.ForeignKey('NGO', on_delete=models.SET('ngo not set'))
    zip = models.IntegerField(blank = True)
    person_of_contact = models.CharField(max_length = 100)
    summary = models.TextField(blank = False)
    story = models.TextField(blank = True)
    # thumbnail = models.ImageField(blank = True)# thumbnail image
    # banner = models.ImageField(blank = True)# banner image
    thumbnail = models.TextField(blank=True)
    gallery1 = models.TextField(blank=True)
    gallery2 = models.TextField(blank=True)
    gallery3 = models.TextField(blank=True)
    gallery4 = models.TextField(blank=True)
    banner = models.TextField(blank=True)
    team_member_id = models.ForeignKey(Team_Member, on_delete=models.SET('team member not set'))
    project_page_desc = models.CharField(max_length=300, blank=True)
    RATINGS = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )
    # rating = models.IntegerField(choices=RATINGS, blank=False)

    def __str__(self):
        return self.title

class NGO(models.Model):
    ngo_id = models.CharField(max_length=10, blank=False, primary_key=True)
    name = models.CharField(max_length = 200, blank = False)
    person_of_contact = models.CharField(max_length=100)
    registration_code = models.BigIntegerField(null = False)
    address = models.CharField(max_length = 200, blank = False)
    website = models.URLField()
    team_member_id = models.ForeignKey(Team_Member, on_delete=models.SET('team member not set'))#FK? #Can be a many-to-many relation?
    project_page_desc = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Consultant(models.Model):
    consultant_id = models.CharField(max_length=10, blank=False, primary_key=True)
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

class Audit(models.Model):
    audit_id = models.CharField(max_length=10, blank=False, primary_key=True)
    date = models.DateField(null=False)
    report_id = models.IntegerField(null = False)#report model needs to be added||Will there be more than one report for a project?
    consultant_id = models.ForeignKey('Consultant', on_delete=models.SET('consultant not set'))
    project_id = models.ForeignKey('Project', on_delete=models.SET('project not set'))

    def __unicode__(self):
        return "%s : %s" % (self.project_id, self.consultant_id)





