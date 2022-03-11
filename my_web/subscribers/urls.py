from . import views
from django.urls import path
from .views import Main_page_sub, subscriptions_user

urlpatterns = [
    path('subscriptions_user', subscriptions_user.as_view(), name="subscriptions"),
    path('Main_page_sub', Main_page_sub.as_view(), name="main_sub")
]
