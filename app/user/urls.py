# from rest_framework.routers import DefaultRouter
from django.urls import path
from user import views

# for using url reverse
app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]
