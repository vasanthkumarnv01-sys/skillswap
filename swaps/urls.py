from django.urls import path
from . import views

urlpatterns = [
    path('send/<int:user_id>/', views.send_request, name='send_request'),
    path('requests/', views.requests_page, name='requests'),
    path('accept/<int:id>/', views.accept_request, name='accept'),
    path('reject/<int:id>/', views.reject_request, name='reject'),
]
