import secrets

from allauth.utils import build_absolute_uri
from django.conf import settings
from django.contrib.auth import get_user_model
from base64 import b64encode
from uuid import uuid4

from django.urls import reverse
from django_short_url.views import get_surl

User = get_user_model()


def generate_api_key_id(count=None):
    if count:
        return secrets.token_urlsafe(count)
    return secrets.token_urlsafe(128)


def generate_unique_key(count=None):
    b64_id = b64encode(uuid4().bytes).decode()
    generated_id = b64_id.rstrip("=").replace("+", "").replace("/", "")
    if count:
        return generated_id[:count]
    return generated_id


# create function to generate random emails
def generate_random_email(count=None, domain="@dummy.com"):
    b64_id = b64encode(uuid4().bytes).decode()
    generated_id = b64_id.rstrip("=").replace("+", "").replace("/", "")
    if count:
        email = generated_id[:count] + domain
    else:
        email = generated_id[:count] + domain
    return email.lower()


# function to generate random anonymous usernames
def generate_random_username(prefix=None):
    if not prefix:
        prefix = "@"
    suffix = secrets.token_urlsafe(8)
    generated_username = "{}{}".format(str(prefix), str(suffix))
    return generated_username


def generate_random_password(user, length=8):
    """
    Provides a random password of the given length.
    :param user: The user to generate a password for.
    :param int length: The length of the password to generate.
    """

    # pwd = "".join([choice(printable) for x in range(int(length))])
    pwd = generate_unique_key(length)
    user.set_password(str(pwd))

    return pwd


def get_shorter_url_login(request):
    """
    Returns a URL that can be used to login to the site using a shorter URL.
    """
    path = get_surl(reverse(settings.LOGIN_URL), length=4)
    return build_absolute_uri(request, path)