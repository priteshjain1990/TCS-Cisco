from django.contrib import admin
from django.urls import path
from router_app import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('router_detail/',views.routerList.as_view()),
    path('router_detail/<int:pk>/',views.routerRUD.as_view()),
    path('token/',views.CustomAuthToken.as_view())
]