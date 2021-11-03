from django.urls import path
from .views import make_announcement, see_log

urlpatterns = [
    path('make-announcement', make_announcement, name='make_announcement'),
    path('', see_log, name='see_log'),
]
