from django.contrib import admin
from django.urls import path, include
from core.views import index
from users.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('cadastro/', register, name='register'),
    path('', include('core.urls')),
    #    path('workouts/', include('workouts.urls')),
    #  path('users/', include('users.urls')),
    path('', index, name='index'),
]
