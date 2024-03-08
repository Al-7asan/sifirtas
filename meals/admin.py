from django.contrib import admin
from .models import MealType, Meal, DayDetails, SubscriptionType, Subscription


class MealTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'added_by')


class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'added_by')


class DayDetailsAdmin(admin.ModelAdmin):
    list_display = ('name', 'day_date', 'meal', 'notes', 'drinks')


class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_days', 'is_active', 'added_by')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
    'user', 'subscription_type', 'start_date', 'end_date', 'delivery_time', 'created_at', 'category', 'is_active')
    filter_horizontal = ('days',)


admin.site.register(MealType, MealTypeAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(DayDetails, DayDetailsAdmin)
admin.site.register(SubscriptionType, SubscriptionTypeAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
