from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..api.serializers import UserSerializer, UserDeactivationSerializer


@extend_schema(exclude=True)
class UserViewSet(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):

        if self.request.user.is_superuser or self.request.user.is_staff:
            qs = get_user_model().objects.all()
        else:
            qs = get_user_model().objects.none()

        return qs

    def get_object(self):
        return self.request.user

    def get_serializer_class(self):
        if self.action == 'deactivate':
            return UserDeactivationSerializer

        return self.serializer_class

    @action(methods=["post"], detail=False)
    def deactivate(self, request, pk=None):
        """
        Returns true if deactivation was successfully
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if request.user.uid == serializer.data.get("uid"):
            request.user.is_active = False
            request.user.save()
            return Response(
                data={"error": False,
                      "message": _(
                                    "Account Deactivation successfully! "
                                    "By deactivating your account, your data will remain valid for 30 days, "
                                    "so you will not be able to register a new account with your same data. "
                                    "If in this period you decide to restore your account, "
                                    "please contact our support team immediately")},
                status=status.HTTP_200_OK,
            )
        return Response(
            data={
                "error": True,
                "message": _("You are not allowed to deactivate this account")
            },
            status=status.HTTP_200_OK)


@extend_schema(exclude=True)
class UserDetailsView(RetrieveUpdateAPIView):
    """
    Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Returns UserModel fields.
    """

    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()

    def get_serializer_context(self):
        return {"request": self.request}