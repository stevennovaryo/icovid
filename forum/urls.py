from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='Forum'),
    path('postToForum/',post_to_forum,name='postToForum')
]
