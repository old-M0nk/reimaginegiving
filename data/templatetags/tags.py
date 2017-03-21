from django import template
from data.models import Project
from users.models import Donor

register = template.Library()


@register.simple_tag()
def fund_percent_achieved(total_amount, raised_amount):
    percent = (raised_amount)*100/(total_amount)
    return format(percent, '.0f')


@register.simple_tag()
def days_left(end, start):
    diff = end-start
    return diff.days


@register.simple_tag()
def no_of_donors(project):
    count = Donor.objects.filter(project=project).count()
    return count



