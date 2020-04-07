from django.urls import path
from apigenerica import views

urlpatterns = [
    path('apigenerica/', views.endopint_list),
    path('apigenerica/<int:pk>/', views.endpoint_detail),
    path('endpoints/<int:pk>/', views.endpoint_detail),
]