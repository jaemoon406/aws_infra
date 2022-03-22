from django.urls import path
from .views import *

urlpatterns = [
    path('api/<int:post_id>', PostView.as_view())
]
