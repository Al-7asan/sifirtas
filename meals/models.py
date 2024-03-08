from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class MealType(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'meal_type'

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(MealType, on_delete=models.DO_NOTHING)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'meal'

    def __str__(self):
        return self.name


class DayDetails(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    day_date = models.DateField()
    meal = models.ForeignKey(Meal, on_delete=models.DO_NOTHING)
    notes = models.TextField(blank=True, null=True)
    drinks = models.TextField(blank=True, null=True, default='no drinks')

    class Meta:
        db_table = 'day_details'

    def __str__(self):
        return f"{self.name} - {self.day_date}"


class SubscriptionType(models.Model):
    name = models.CharField(max_length=255)
    number_of_days = models.IntegerField()
    is_active = models.BooleanField(default=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'subscription_type'

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_type = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE, null=False)
    days = models.ManyToManyField(DayDetails)  # Relationship with DayDetails
    start_date = models.DateField()
    end_date = models.DateField()
    overall_notes = models.TextField(blank=True, null=True)
    delivery_notes = models.TextField(blank=True, null=True)
    delivery_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=5, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'subscription'

    def __str__(self):
        return f"{self.user}'s subscription"
