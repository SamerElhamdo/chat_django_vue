from django.urls import path
from .views import MessageAPIView

urlpatterns = [
    path('messages/<str:chat_id>', MessageAPIView.as_view())
]
