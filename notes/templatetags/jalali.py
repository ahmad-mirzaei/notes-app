import jdatetime
from django import template

register = template.Library()

@register.filter
def jalali(value):
    if not value:
        return ""

    return jdatetime.datetime.fromgregorian(
        datetime=value
    ).strftime("%Y/%m/%d %H:%M")