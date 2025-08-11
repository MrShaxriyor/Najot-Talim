from django.urls import path
from .views import *
urlpatterns = [
    path('', NajotTalimAPIView.as_view()),
    path('reg/', RegisterView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    # path('d/<int:pk>/', NajotTalimDetailAPIView.as_view()),
]
