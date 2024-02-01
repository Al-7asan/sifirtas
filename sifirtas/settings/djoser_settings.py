from datetime import timedelta

DJOSER = {
    'SERIALIZERS': {
        'user_create_password_retype':'users.serializers.CustomUserSerializer'
    },
    'SEND_ACTIVATION_EMAIL': False,  # If you don't want to send activation emails
    'PASSWORD_RESET_CONFIRM_URL': '/password-reset/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE': True,
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}
