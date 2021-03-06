from django import template
import datetime
from users.models import Donation, Card_Details

register = template.Library()


@register.simple_tag()
def fund_percent_achieved(total_amount, raised_amount):
    percent = (raised_amount)*100/(total_amount)
    return format(percent, '.0f')


@register.simple_tag()
def days_left(end):
    diff = end-datetime.date.today()
    return diff.days


@register.simple_tag()
def no_of_donors(project):
    count = Donation.objects.filter(project_id=project).count()
    return count


@register.simple_tag()
def days_gap(project):
    count = Donation.objects.filter(project_id=project).count()
    return count



@register.simple_tag()
def cardno(card):
    card = Card_Details.objects.filter(card_number=card.card_number)
    num = card.card_number[-4:]
    return num


