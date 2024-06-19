from django.urls import path
from airbnb import views

urlpatterns = [
	path('', views.main, name='main'),
    path('signup', views.signup, name='signup'),
	path('signin', views.signin, name='signin'),
	path('create-property', views.create_property, name='create-properties'),
    path('logout', views.logout, name='logout'),
    path('properties', views.api_properties)
]
