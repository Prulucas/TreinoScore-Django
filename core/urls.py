from django.urls import path
from .views import contact
from core.views import index

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('', index, name='index'),
]
