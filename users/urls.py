from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]