from . import views
from django.urls import path

urlpatterns =[
path('',views.index,name='index'),
path('signup/',views.signup,name='signup'),
path('login/',views.login_user,name='login'), 
# path('get-nearest-facility/',views.nearest_facility),
path('get-features/',views.get_features)
]