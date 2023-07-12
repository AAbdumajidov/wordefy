from django.urls import path
from .views import ContactListCreateView


urlpatterns = [
    path('list-create/', ContactListCreateView.as_view()),
]