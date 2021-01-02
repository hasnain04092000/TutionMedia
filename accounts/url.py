from django.urls import path
from .views import register_view,logout_view,login_view, updateAccount, ProfileView, ProfileUpdateView


urlpatterns = [
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('update/', updateAccount, name='update_account'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('profile-update/',ProfileUpdateView.as_view(), name='profile_update'),
]