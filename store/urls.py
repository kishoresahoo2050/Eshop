from django.urls import path
from . import views
from .middlewares.auth_middle import Authenticate_Middel


urlpatterns = [
    path('',views.index,name='home'),
    path('signup/',views.signup,name="signup"),
    path('logins/',views.LoginUser.as_view(),name='login'),
    path('logout/',views.Logout.as_view(),name="logout"),
    path('cart/',Authenticate_Middel(views.Cart),name="cart"),
    path('orders/',Authenticate_Middel(views.All_Orders),name="orders")

]
