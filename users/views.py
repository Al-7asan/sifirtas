from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # print("triggered")
        response = super().post(request, *args, **kwargs)
        # Decode the access token to extract user ID
        if 'access' in response.data:
            token_string = response.data['access']
            token_instance = AccessToken(token=token_string)
            user_id = token_instance['user_id']
            # Fetch the user object using the user ID
            User = get_user_model()
            user = User.objects.get(id=user_id)
            # Add custom user information to the token payload
            response.data['user_id'] = user.id  # Add user ID to payload
            response.data['phone_number'] = user.phone_number  # Add email to payload
            response.data['gender'] = user.gender  # Add email to payload
            response.data['date_of_birth'] = user.date_of_birth  # Add email to payload
            # Add other custom claims as needed
            response.data['access'] = str(token_instance)
        return response
