from django import template

register = template.Library()

@register.simple_tag()
def fund_percent_achieved(total_amount, raised_amount):
    percent = (raised_amount)*100/(total_amount)
    return format(percent, '.0f')