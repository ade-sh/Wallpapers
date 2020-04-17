from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='account'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_form, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
