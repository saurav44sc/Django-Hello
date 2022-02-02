from django.contrib import admin
from django.urls import path, include
from core.views import PostListCreateView

urlpatterns = [
    path('', PostListCreateView.as_view(), name="test"),

]