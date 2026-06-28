import jdatetime
from django import template
from django.utils import timezone

# Create here.

register = template.Library()

@register.filter
def jalali(value):
    if not value:
        return ""

    # تبدیل به ساعت تهران
    value = timezone.localtime(value)

    # تبدیل به تاریخ شمسی
    jdate = jdatetime.datetime.fromgregorian(datetime = value)

    return jdate.strftime("%Y/%m/%d %H:%M")