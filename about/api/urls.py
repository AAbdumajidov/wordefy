from django.urls import path
from .views import FeedbackListCreateAPIVIew, FeedbackRUDVIew


urlpatterns = [
    path('list-create/', FeedbackListCreateAPIVIew.as_view()),
    path('rud/<int:pk>/', FeedbackRUDVIew.as_view()),
]
