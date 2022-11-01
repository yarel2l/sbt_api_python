from django.conf import settings
from django.contrib.auth.models import UserManager
from model_utils.managers import InheritanceManagerMixin


class UserInheritanceManager(InheritanceManagerMixin, UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        if 'username' in extra_fields:
            username = self.model.normalize_username(extra_fields.pop('username'))
            extra_fields.update({'username': username})

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        if "allauth" in settings.INSTALLED_APPS:
            from allauth.account.models import EmailAddress
            emailaddress, created = EmailAddress.objects.get_or_create(user=user, email=user.email)
            emailaddress.verified = True
            emailaddress.primary = True
            emailaddress.save()

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)