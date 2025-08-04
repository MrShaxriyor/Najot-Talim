from django.urls import path
from .views import *
urlpatterns = [
    path('', NajotTalimAPIView.as_view()), 
    path('d/<int:pk>/', NajotTalimDetailAPIView.as_view()),
]
