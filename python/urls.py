from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('TempMail/', include('TempMail.urls')),
    path('login/', views.loginPage, name="login"),
    path('', views.signupPage, name="signup"),
    path('home/', views.homePage, name="home"),
    path('forgetpassword/', views.forgetPasswordPage, name="forgetpassword"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]