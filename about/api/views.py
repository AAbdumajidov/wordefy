from .serializers import FeedbackSerializer
from rest_framework import generics
from ..models import Feedback
from .permissions import IsAdminUserOrReadOnly


class FeedbackListCreateAPIVIew(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class FeedbackRUDVIew(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


