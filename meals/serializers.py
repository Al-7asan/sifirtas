from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Subscription, DayDetails


class DayDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayDetails
        fields = '__all__'

    def update(self, request, *args, **kwargs):
        if 'user' in self.validated_data:
            raise ValidationError("Updating the 'user' field is not allowed.")
        self.validated_data.pop('user', None)
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


class SubscriptionCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    days = DayDetailsSerializer(many=True)  # Nested serializer for DayDetails

    class Meta:
        model = Subscription
        fields = '__all__'

    def update(self, request, *args, **kwargs):
        if 'user' in self.validated_data:
            raise ValidationError("Updating the 'user' field is not allowed.")
        self.validated_data.pop('user', None)
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)


    def create(self, validated_data):
        if not 'days' in validated_data:
            raise serializers.ValidationError({"days": "Missing required field"})
        days_data = validated_data.pop('days')  # Extract nested DayDetails data
        subscription = Subscription.objects.create(**validated_data)  # Create Subscription instance

        # List to store any errors that occur during creation of DayDetails instances
        errors = []

        # Loop through each day_data and create DayDetails instances
        for day_data in days_data:
            try:
                # Create DayDetails instance and associate it with the Subscription
                day = DayDetails.objects.create(subscription=subscription, **day_data)
                subscription.days.add(day)
            except Exception as e:
                # If an error occurs, append the error message to the errors list
                errors.append(str(e))

        # If there were errors during creation, raise a ValidationError with the error messages
        if errors:
            raise serializers.ValidationError(errors)

        return subscription


class SubscriptionGetSerializer(serializers.ModelSerializer):
    days = DayDetailsSerializer(many=True, read_only=True)  # Nested serializer for DayDetails

    class Meta:
        model = Subscription
        fields = '__all__'  # Adjust according to your retrieval needs
