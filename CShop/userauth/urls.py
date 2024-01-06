from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup_user.as_view(),name='signup'),
    path('login/',views.login_user.as_view(),name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.userlogout,name='logout'),
    path('changedata/<int:id>',views.changeuserdata.as_view(),name='changedata'),
    path('changepassword/',views.passchange,name='passchange1'),
    path('changepassword1/',views.passchangewithoutprev,name='passchange2')
]