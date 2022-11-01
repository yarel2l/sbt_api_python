from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from allauth.account.signals import user_signed_up
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_text
from django_short_url.views import get_surl


class AccountingAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        if hasattr(request, 'session') and request.session.get(
                'account_verified_email'):
            return True
        else:
            # Site is open to signup
            return False

    def get_user_signed_up_signal(self):
        return user_signed_up

    def format_email_subject(self, subject):
        prefix = settings.ACCOUNT_EMAIL_SUBJECT_PREFIX
        if prefix is None:
            site = Site.objects.get_current()
            prefix = "[{name}] ".format(name=site.name)
        return f"{prefix} {force_text(subject)}"

    def render_mail(self, template_prefix, email, context):
        """
        Renders an e-mail to `email`.  `template_prefix` identifies the
        e-mail that is to be sent, e.g. "account/email/email_confirmation"
        """
        subject = render_to_string('{0}_subject.txt'.format(template_prefix),
                                   context)
        # remove superfluous line breaks
        subject = " ".join(subject.splitlines()).strip()
        subject = self.format_email_subject(subject)

        bodies = {}
        for ext in ['html', 'txt']:
            try:
                template_name = '{0}_message.{1}'.format(template_prefix, ext)
                bodies[ext] = render_to_string(template_name,
                                               context).strip()
            except TemplateDoesNotExist:
                if ext == 'txt' and not bodies:
                    # We need at least one body
                    raise
        if 'txt' in bodies:
            msg = EmailMultiAlternatives(subject,
                                         bodies['txt'],
                                         context.get('from_email', None) or settings.DEFAULT_FROM_EMAIL,
                                         [email])
            if 'html' in bodies:
                msg.attach_alternative(bodies['html'], 'text/html')
        else:
            msg = EmailMessage(subject,
                               bodies['html'],
                               context.get('from_email', None) or settings.DEFAULT_FROM_EMAIL,
                               [email])
            msg.content_subtype = 'html'  # Main content is now text/html
        return msg

    def send_mail(self, template_prefix, email, context):
        msg = self.render_mail(template_prefix, email, context)
        msg.send()

    def clean_email(self, email):
        """
        Validates an email value. You can hook into this if you want to
        (dynamically) restrict what email addresses can be chosen.
        """
        return email

    def add_message(self, request, level, message_template,
                    message_context=None, extra_tags=''):
        """
        Wrapper of `django.contrib.messages.add_message`, that reads
        the message text from a template.
        """
        if 'django.contrib.messages' in settings.INSTALLED_APPS:
            try:
                if message_context is None:
                    message_context = {}
                message = render_to_string(message_template,
                                           message_context).strip()
                if message:
                    messages.add_message(request, level, message,
                                         extra_tags=extra_tags)
            except TemplateDoesNotExist:
                pass


class CustomAllauthAdapter(AccountingAdapter):

    def stash_verified_email(self, request, email):
        request.session['account_verified_email'] = email

    def unstash_verified_email(self, request):
        ret = request.session.get('account_verified_email')
        request.session['account_verified_email'] = None
        return ret

    def get_email_confirmation_redirect_url(self, request):
        """
        Redirect to next if in request GET params, used to properly redirect to checkout page after sign up though
        session cart
        :param request:
        :return: url
        """
        return super(CustomAllauthAdapter, self).get_email_confirmation_redirect_url(request)

    def get_email_confirmation_url(self, request, emailconfirmation):
        """Constructs the email confirmation (activation) url.

        Note that if you have architected your system such that email
        confirmations are sent outside of the request context `request`
        can be `None` here.
        """
        url = reverse("account_confirm_email", args=[emailconfirmation.key])
        surl = get_surl(url, 4)
        ret = build_absolute_uri(request, surl)
        return ret

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        """ Generate token with proper next={url} """

        current_site = settings.SITE_NAME
        domain = request.get_host()

        activate_url = self.get_email_confirmation_url(request, emailconfirmation)

        ctx = {
            "user": emailconfirmation.email_address.user,
            "activate_url": activate_url,
            "site_name": current_site,
            "domain": domain,
            'next': request.POST.get('next')
        }

        if signup:
            email_template = 'account/email/email_confirmation_signup'
        else:
            email_template = 'account/email/email_confirmation'

        self.send_mail(email_template,
                       emailconfirmation.email_address.email,
                       ctx)