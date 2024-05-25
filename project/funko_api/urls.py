from django.urls import path
from funko_api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('funkos_rest/', views.funkos_rest, name='funkos_rest'),
]

# from django.urls import path

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('funkos_rest/', views.funkos_rest, name='funkos_rest'),
#     path('users_rest/', views.users_rest, name='users_rest'),
#     path('add_funko/', views.add_funko_view, name='add_funko'),
# ]