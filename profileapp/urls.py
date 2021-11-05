from django.urls import path
from . import views

urlpatterns = [
    path('profile-page/', views.profile, name='user-profile'),
    path('edit-profile/', views.profileupdate, name='update-profile'), 
    path('profile-datas/', views.profiledatas, name='profile-datas'),
    path('profile/<int:id>', views.otheruserprofile, name='otherprofile'),
]