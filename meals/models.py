from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class DayDetails(models.Model):
    DAYS_CHOICES = [
        ('Mo', 'Monday'),
        ('Tu', 'Tuesday'),
        ('We', 'Wednesday'),
        ('Th', 'Thursday'),
        ('Sa', 'Saturday'),
        ('Su', 'Sunday'),
    ]
    day = models.CharField(max_length=2, choices=DAYS_CHOICES, null=False, blank=False)
    meal = models.CharField(max_length=500, blank=False, null=False)
    notes = models.TextField(blank=True, null=True)
    drinks = models.TextField(blank=True, null=True, default='no drinks')

    def __str__(self):
        return self.day


class Subscription(models.Model):
    Subscription_CHOICES = [
        ('3D', _('3 Days')),
        ('5D', _('5 Days')),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=2, choices=Subscription_CHOICES)
    days = models.ManyToManyField(DayDetails)  # Relationship with DayDetails
    overall_notes = models.TextField(blank=True, null=True)
    delivery_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s subscription - {self.get_subscription_type_display()}"
