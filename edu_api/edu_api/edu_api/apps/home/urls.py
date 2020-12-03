from django.urls import path
from home import views

urlpatterns = [
    path('banners/', views.BannerAPIView.as_view()),
    path('footer/', views.NavAPIView.as_view()),
    path('header/', views.NavvAPIView.as_view()),
]
