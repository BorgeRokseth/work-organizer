from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.NextActionDetailApiView.as_view(), name='next-action-details'),
    path('', views.NextActionListApiView.as_view(), name='next-action-list'),
]