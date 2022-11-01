from django import template

from .utils import get_profile_timezone_form_context, get_profile_scripts_context

register = template.Library()


@register.inclusion_tag('iam/profile/modal_timezone.html', takes_context=True)
def show_timezone_modal(context):
    template_context = get_profile_timezone_form_context(context)
    return template_context


@register.inclusion_tag('iam/profile/scripts.html', takes_context=True)
def render_profile_scripts(context):
    template_context = get_profile_scripts_context(context)
    return template_context