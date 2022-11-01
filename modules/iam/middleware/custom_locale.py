from django.conf import settings
from django.middleware.locale import LocaleMiddleware
from django.urls import is_valid_path
from django.utils import translation


class CustomLocaleMiddleware(LocaleMiddleware):

    def process_response(self, request, response):
        response = super().process_response(request, response)
        language = translation.get_language()
        user = request.user

        # FIXME: Update this to get tenant urlconf
        urlconf = getattr(request, "urlconf", settings.ROOT_URLCONF)

        if user and user.is_authenticated:
            if user.preferred_language and user.preferred_language != language:
                translation.activate(user.preferred_language)

                preferred_language = translation.get_language()
                language_path = f"/{preferred_language}{request.path_info[3:]}"

                path_valid = is_valid_path(language_path, urlconf)

                if path_valid:
                    request.session[translation.LANGUAGE_SESSION_KEY] = preferred_language
                    request.LANGUAGE_CODE = preferred_language
                    return self.response_redirect_class(language_path)

        return response
