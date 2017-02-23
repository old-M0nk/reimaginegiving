from __future__ import unicode_literals

from django.db import models

class Team_Member(models.Model):
    team_member_id = models.CharField(max_length=10, blank=False)
    name = models.CharField(max_length = 120, blank = False)
    def __unicode__(self):
        return self.name

