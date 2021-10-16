from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.InItemDetailApiView.as_view(), name='in-item-details'),
    path('', views.InItemListApiView.as_view(), name='in-item-list'),
]