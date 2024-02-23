from . import views
from django.urls import path

urlpatterns =[
path('',views.index,name='index'),
path('get-nearest-facility/',views.nearest_facility),
]