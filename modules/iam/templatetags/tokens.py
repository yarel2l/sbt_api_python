from django import template

register = template.Library()


@register.filter
def show_token(token):
    return "{}...{}".format(token[:10], token[-50:])
