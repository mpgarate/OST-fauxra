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

    value = re.sub(r'(http[s]{0,1}://[\w]*\.[\w\/\.]*[^\s])',
                   r'<a href="\1" target="_blank">\1</a>', value)

    # wrap image urls with img tag
    # to avoid double-wrapping urls, this regex takes advantage of the fact that
    # any image urls of interest will be surrounded by the > and < characters of
    # the surrounding anchor tag.
    value = re.sub(r'>(http[s]{0,1}://[\w]*\.[\w\/\.]*\.((jpg)|(png)|(gif)))<',
                   r'><img src="\1" alt="embedded image" /><', value)

    return value
