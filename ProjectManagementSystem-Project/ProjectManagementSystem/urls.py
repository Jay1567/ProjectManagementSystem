from django.contrib import admin
from django.urls import path, include

api_version = 'api/v1/'

urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),

    path(api_version+'rest-auth/', include('dj_rest_auth.urls')),
    path(api_version+'rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]
