from django import template
register = template.Library()

@register.filter
def split(value, separator="\n"):
    if not value:
        return []
    return [s.strip() for s in str(value).split(separator) if s.strip()]

@register.filter
def strip(value):
    if not value:
        return value
    return str(value).strip()
