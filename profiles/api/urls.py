from django.urls import path
from .views import ProfileListCreateView


urlpatterns = [
    path('list-create/', ProfileListCreateView.as_view())
]