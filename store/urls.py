from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='home'),
    path('signup/',views.signup,name="signup"),
    path('logins/',views.LoginUser.as_view(),name='login')
]
