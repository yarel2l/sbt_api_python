from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import cache_page
from django.views.i18n import JavaScriptCatalog

# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView,
# )

admin.site.site_header = _("SCORBOT API - Support Panel")
admin.site.site_title = _("SCORBOT API - Support Panel")


last_modified_date = timezone.now()

urlpatterns = [
    path('jsi18n/',
             cache_page(86400, key_prefix='js18n-%s' % last_modified_date)(
                 JavaScriptCatalog.as_view(
                     packages=[
                        'core',
                        'iam',
                        'tournaments',
                     ]
                 )
             ),
             name='javascript-catalog'),

    re_path(r'^s/', include('django_short_url.urls', namespace='django_short_url')),

    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # path('api/auth-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/auth-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/auth-token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('api/v1/', include('v1.urls')),

]

urlpatterns += i18n_patterns(

    path("auth/", include("allauth.urls")),
    path("accounts/", include("iam.urls")),
    path('support/', admin.site.urls),
    path("select2/", include("django_select2.urls")),
    path('', include('core.urls')),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
