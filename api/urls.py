from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.SignupUserView.as_view(), name='signup'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path("user-profile/", views.UserProfileView.as_view(), name="user-profile"),
    path("user-profile/<int:user_id>", views.UserProfileNew.as_view(), name="user-profile-new"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("ResetPassword/", views.ResetPassword.as_view(), name="ResetPassword")
    
]
