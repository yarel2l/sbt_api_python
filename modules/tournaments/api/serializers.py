import random

import pytz
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from core.api.serializers import (
    StatusSerializer, TimezoneSerializer
)
from core.models import (
    ScorbotTimezone, ScorbotEventType, ScorbotStatus,
)
from organizations.api.serializers import OrganizationsSerializer
from organizations.models import ScorbotOrganization
from users.api.serializers import ScorbotUserSerializer
from users.models import ScorbotUser
from ..models import (
    Tournament,
    TournamentInformation, TournamentUser,
)


class TournamentInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentInformation
        fields = ["letterid", "letter", "username", "flyerurl"]
        read_only_fields = ["letterid", "username"]


class TournamentUserSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = TournamentUser
        fields = ["user", "isowner", "lastupdate"]

    def get_user(self, obj):
        try:
            user = ScorbotUser.objects.using("scorbot").get(userid=obj.userid.userid)
            return ScorbotUserSerializer(user).data
        except ScorbotUser.DoesNotExist:
            return None


class TournamentSerializer(serializers.ModelSerializer):
    organization = OrganizationsSerializer(read_only=True)
    information = TournamentInformationSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    state = serializers.SerializerMethodField()
    eventtype = serializers.SerializerMethodField()
    timezone = TimezoneSerializer(read_only=True)
    tournament_users = TournamentUserSerializer(many=True, read_only=True)

    class Meta:
        model = Tournament
        fields = ["event_number", "name", "status", "active", "startdate", "enddate",
                  "eventtype", "genderdesc", "website",
                  "contactname", "contactphone", "contactemail",
                  "city", "state", "timezone", "gameduration",
                  "registrationpriceperteam", "registrationfee", "registrationstartdate", "registrationenddate",
                  "registrationcountteams", "registrationdiscount",
                  "smsid", "organization",
                  "information", "tournament_users"]
        read_only_fields = ["event_number"]

    def get_eventtype(self, obj):
        if obj.eventtype:
            return obj.eventtype.descr
        return None

    def get_state(self, obj):
        if obj.state:
            return str(obj.state)
        return None


class TournamentCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True,)
    contact_name = serializers.CharField(required=True, write_only=True)
    contact_phone = PhoneNumberField(required=True, write_only=True)
    contact_email = serializers.EmailField(required=True, write_only=True)
    start_date = serializers.DateTimeField(required=True, write_only=True)
    end_date = serializers.DateTimeField(required=True, write_only=True)
    duration = serializers.IntegerField(required=True, write_only=True)
    organization = serializers.IntegerField(required=False, allow_null=True, write_only=True)
    city = serializers.CharField(required=True,)
    state = serializers.CharField(required=True)

    event_type = serializers.PrimaryKeyRelatedField(queryset=ScorbotEventType.objects.using("scorbot").all(),
                                                    required=True,
                                                    write_only=True)
    timezone = serializers.PrimaryKeyRelatedField(required=True,
                                                  queryset=ScorbotTimezone.objects.using("scorbot").all())

    information = TournamentInformationSerializer(required=False, allow_null=True)

    registrationpriceperteam = serializers.DecimalField(required=False, allow_null=True, max_digits=6, decimal_places=2)
    registrationfee = serializers.DecimalField(required=False, allow_null=True, max_digits=6, decimal_places=2)
    registrationstartdate = serializers.DateTimeField(required=False, allow_null=True)
    registrationenddate = serializers.DateTimeField(required=False, allow_null=True)
    registrationcountteams = serializers.IntegerField(required=False, allow_null=True)
    registrationdiscount = serializers.DecimalField(required=False, allow_null=True, max_digits=6, decimal_places=2)

    class Meta:
        model = Tournament
        fields = ["event_number", "name", "event_type", "contact_name", "contact_phone", "contact_email",
                  "start_date", "end_date", "city", "state", "timezone", "duration",
                  "organization",
                  "smsid", "robot",
                  "information",
                  "registrationpriceperteam", "registrationfee", "registrationstartdate", "registrationenddate",
                  "registrationcountteams", "registrationdiscount"
                  ]
        read_only_fields = ["event_number"]

    def validate(self, attrs):
        # compare tournament dates start_date and end_date
        tz_info = pytz.UTC

        if attrs['start_date'].replace(tzinfo=tz_info) > attrs['end_date'].replace(tzinfo=tz_info):
            raise serializers.ValidationError({"invalid_date": _("Start date must be less than end date")})

        # validate start date and current date
        if attrs['start_date'].replace(tzinfo=tz_info) < timezone.now():
            raise serializers.ValidationError({"invalid_date": _("Start date must be greater than current date")})

        if attrs['end_date'].replace(tzinfo=tz_info) < timezone.now():
            raise serializers.ValidationError({"invalid_date": _("End date must be greater than current date")})

        if attrs['event_type'] not in ScorbotEventType.objects.using("scorbot").all():
            raise serializers.ValidationError({"invalid_event_type": _("Invalid event type")})

        # validate game duration
        if attrs['duration'] < 0:
            raise serializers.ValidationError({"invalid_duration": _("Duration must be a positive number")})

        # Validate that state is a valid choice
        # state field must have two characters
        if len(attrs['state']) != 2:
            raise serializers.ValidationError({"invalid_state": _("Invalid state")})
        # check if state is in the state list, then assign the state object to the state field
        # else then register the state and assign the state object to the state field
        # try:
        #     state = ScorbotState.objects.using("scorbot").get(state=attrs['state'])
        # except ScorbotState.DoesNotExist:
        #     state = ScorbotState.objects.using("scorbot").create(state=attrs['state'].upper())
        # attrs['state'] = state

        # Validate that timezone is a valid choice
        if attrs['timezone'] not in ScorbotTimezone.objects.using("scorbot").all():
            raise serializers.ValidationError({"invalid_tz": _("Invalid timezone")})

        # Validate that organization is a valid choice
        if 'organization' not in attrs or attrs['organization'] is None:
            attrs['organization'] = None
        else:
            try:
                org = ScorbotOrganization.objects.using("scorbot").get(id=attrs['organization'])
                attrs['organization'] = org
            except ScorbotOrganization.DoesNotExist:
                raise serializers.ValidationError({"invalid_org": _("Invalid organization")})

        if 'registrationpriceperteam' not in attrs or attrs['registrationpriceperteam'] is None:
            attrs['registrationpriceperteam'] = 0

        if 'registrationfee' not in attrs or attrs['registrationfee'] is None:
            attrs['registrationfee'] = 0

        if 'registrationcountteams' not in attrs or attrs['registrationcountteams'] is None:
            attrs['registrationcountteams'] = 0

        if 'registrationdiscount' not in attrs or attrs['registrationdiscount'] is None:
            attrs['registrationdiscount'] = 0

        if 'registrationstartdate' not in attrs or attrs['registrationstartdate'] is None:
            attrs['registrationstartdate'] = attrs['start_date']

        if 'registrationenddate' not in attrs or attrs['registrationenddate'] is None:
            attrs['registrationenddate'] = attrs['end_date']

        if 'information' not in attrs or attrs['information'] is None:
            attrs['information'] = None

        return attrs

    def create(self, validated_data):
        # Get tournament status for new tournaments
        status = ScorbotStatus.objects.using("scorbot").get(statusid=8)     # 8 = New

        # create tournament
        tournament = Tournament.objects.using("scorbot").create(
            name=validated_data['name'],
            eventtype=validated_data['event_type'],
            contactname=validated_data['contact_name'],
            contactphone=validated_data['contact_phone'],
            contactemail=validated_data['contact_email'],
            startdate=validated_data['start_date'],
            enddate=validated_data['end_date'],
            city=validated_data['city'],
            state=validated_data['state'],
            timezone=validated_data['timezone'],
            gameduration=validated_data['duration'],
            organization=validated_data['organization'],
            smsid=validated_data['smsid'],
            robot=validated_data['robot'],

            registrationpriceperteam=validated_data['registrationpriceperteam'],
            registrationfee=validated_data['registrationfee'],
            registrationstartdate=validated_data['registrationstartdate'],
            registrationenddate=validated_data['registrationenddate'],
            registrationcountteams=validated_data['registrationcountteams'],
            registrationdiscount=validated_data['registrationdiscount'],

            status=status,
            maxpoints=15,
            active=False,
        )

        # Check if exist one scorbot user with contact email or contact or create a new user and link to tournament
        try:
            user = ScorbotUser.objects.using("scorbot").get(textingphone=validated_data['contact_phone'])
        except ScorbotUser.DoesNotExist:
            otp = random.randint(100000, 999999)
            user = ScorbotUser.objects.using("scorbot").create(
                textingphone=validated_data['contact_phone'],
                email=validated_data['contact_email'],
                name=validated_data['contact_name'],
                username=validated_data['contact_email'],
                utype=2,
                active=1,
                pword=make_password(str(validated_data['contact_email'])),
                creationdate=timezone.now(),
                lastupdate=timezone.now(),
                usermembership_id=4,
                activationcode=otp,
            )

        TournamentUser.objects.using("scorbot").get_or_create(
            tournamentid=tournament,
            userid=user,
            defaults={
                'lastupdate': timezone.now(),
                'isowner': 1
            }
        )

        # create tournament information
        if validated_data['information']:
            if 'letter' in validated_data['information']:
                letter = validated_data['information']['letter']
            else:
                letter = None
            if 'flyerurl' in validated_data['information']:
                flyerurl = validated_data['information']['flyerurl']
            else:
                flyerurl = None

            TournamentInformation.objects.using("scorbot").create(
                tournamentid=tournament,
                letter=letter,
                flyerurl=flyerurl,
                username=user.username,

            )

        return tournament