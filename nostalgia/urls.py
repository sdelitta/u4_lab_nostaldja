from django.urls import path
from . import views

urlpatterns = [
    path('', views.decade_list, name='decade'),
    path('fads/', views.fad_list, name="fad_list"),
    path('decades/<int:pk>', views.decade_details, name='decade_details'),
    path('fads/<int:pk>', views.fad_details, name='fad_details')
]