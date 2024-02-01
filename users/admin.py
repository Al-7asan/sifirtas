# myapp/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone_number', 'date_of_birth', 'gender')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'phone_number', 'date_of_birth', 'gender')


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'phone_number', 'date_of_birth', 'gender', 'is_superuser')
    search_fields = ('email', 'phone_number')
    ordering = ('email',)
    list_filter = ('gender', 'date_of_birth')
    exclude = ('username', 'first_name', 'last_name')  # Exclude the undesired fields

    add_fieldsets = (
        (None, {
            'fields': ('email', 'phone_number', 'date_of_birth', 'gender', 'password1', 'password2'),
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'groups', 'user_permissions'),
        }),
    )

    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'date_of_birth', 'gender', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'groups', 'user_permissions')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
