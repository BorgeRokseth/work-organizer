from django.urls import path

from . import views

urlpatterns = [
    path('next-actions/<int:pk>/', views.NextActionDetailApiView.as_view(), name='next-action-details'),
    path('next-actions/', views.NextActionListApiView.as_view(), name='next-action-list'),
    path('contexts/', views.ContextListApiView.as_view(), name="context-list"),
    path('active-projects/', views.ActiveProjectListApiView.as_view(), name="active-projects-list")
]