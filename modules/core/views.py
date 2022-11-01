from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class ControlPanelView(LoginRequiredMixin, TemplateView):
    template_name = "core/control_panel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Control Panel')
        return context