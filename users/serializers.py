from datetime import datetime
from re import match

from djoser.serializers import UserCreatePasswordRetypeSerializer
from rest_framework import serializers


class CustomUserSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = ('phone_number', 'gender', 'date_of_birth', 'password', 'email')
        required_fields = ['phone_number', 'gender', 'date_of_birth', 'password']
    def validate_phone_number(self, value):
        if match("07([5789])[0-9]{8}$", value) is None:
            raise serializers.ValidationError('Invalid phone number format.')
        return value

    def validate_date_of_birth(self, value):
        # Assuming date_of_birth is in the format 'YYYY-MM-DD'

        current_date = datetime.now()

        # Calculate the difference in years
        age = current_date.year - value.year - (
                (current_date.month, current_date.day) < (value.month, value.day))
        if int(age) < 14 or int(age) > 100:
            raise serializers.ValidationError('Invalid date.')
        return value
