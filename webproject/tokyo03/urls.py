from django.urls import path
from . import views
from .views import Listtokyo03View,RecommendationView

urlpatterns = [
    path('', Listtokyo03View.as_view(), name='list_tokyo03'),
    path('Recommendation/<int:pk>/',RecommendationView.as_view(), name='recommendation-detail'),
    ]

