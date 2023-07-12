from rest_framework import generics
from .serializers import ProfileSerializer
from ..models import Profile


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer