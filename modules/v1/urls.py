from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('organization/', include('organizations.api.urls')),
    path('division/', include('divisions.api.urls')),
    path('event/', include('tournaments.api.urls')),
    path('team/', include('teams.api.urls')),

    path('iam/', include('iam.api.urls')),
    path('', include('core.api.urls')),

]