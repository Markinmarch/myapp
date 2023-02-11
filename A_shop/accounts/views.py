from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle


from accounts.permissions import IsOwnerOrReadOnly
from accounts.serializers import ProfileSerializer
from accounts.models import Profiles



class ProfileViewSet(ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        # IsAuthenticated,
        IsOwnerOrReadOnly
    ]
    throttle_classes = [
        AnonRateThrottle,
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)