from django.urls import path
from home.views import index,edit_feedback,delete_feedback


urlpatterns = [
    path('', index,name='index'),
    path('edit_feedback', edit_feedback, name='edit_feedback'),
    path('delete_feedback', delete_feedback, name='delete_feedback'),
    # TODO Add friends path using friend_list Views
]
