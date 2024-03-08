from django.urls import path
from .import views


urlpatterns = [
    path('details/<int:id>',views.detail,name='details'),
    path('buy/<int:id>',views.buy,name='buynow')

]

