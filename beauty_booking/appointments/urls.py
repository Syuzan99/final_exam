from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('specialist/<int:specialist_id>/', views.specialist_profile, name='specialist_profile'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('contact-support/', views.contact_support, name='contact_support'),

]
