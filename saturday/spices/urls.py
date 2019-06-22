from django.urls import include, path
from . import views
app_name = 'spices'

urlpatterns = [
    path('', views.spice_mix_list, name='list'),
    path('spice/<int:spice_id>/', views.spice, name='spice'),
    path('mix/<int:spice_mix_id>/', views.spice_mix, name='mix'),
    path('add', views.add, name='add'),
    path('add_post', views.add_post, name='add_post'),
]