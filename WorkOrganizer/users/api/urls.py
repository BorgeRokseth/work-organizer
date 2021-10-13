from django.urls import path
from users.api.views import CurrentUserApi


urlpatterns = [
    path("user/", CurrentUserApi.as_view(), name="current-user")
]