import re

from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
@stringfilter
def replace_urls(value):
    # wrap image urls with img tag
    # value = re.sub(r'(http[s]{0,1}://[\w]*\.[\w\/\.]*[^\s"\'"])',
    #                r'<img src="\1" />', value)


    # wrap all urls with anchor tag
    value = re.sub(r'(http[s]{0,1}://[\w]*\.[\w\/\.]*[^\s]([\s]|$)((?!\.jpg)))',
                   r'<a href="\1" target="_blank">\1</a>', value)

    # wrap image urls with img tag
    value = re.sub(r'>(http[s]{0,1}://[\w]*\.[\w\/\.]*\.jpg)<',
                   r'><img src="\1" /><', value)

    return value
