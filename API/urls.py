from django.urls import path
from .views import *
urlpatterns = [
    path('', NajotTalimListView.as_view()), 
    path('d/<int:pk>/', NajotTalimDetailView.as_view()),
]
