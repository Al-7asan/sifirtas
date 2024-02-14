from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Subscription
from .serializers import SubscriptionCreateSerializer, SubscriptionGetSerializer


class SubscriptionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return SubscriptionCreateSerializer
        else:
            return SubscriptionGetSerializer

    def get_queryset(self):
        user = self.request.user
        return Subscription.objects.filter(user=user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        super().destroy(request, *args, **kwargs)
        return Response({"message": "Object deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
