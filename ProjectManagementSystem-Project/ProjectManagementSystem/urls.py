from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from dj_rest_auth.registration.views import ConfirmEmailView
from django.views.generic import TemplateView

api_version = 'api/v1/'

urlpatterns = [
        path('', include('frontend.urls')),
        path('admin/', admin.site.urls),

        path('api/v1/project/', include('project.urls')),

        path(api_version+'rest-auth/', include('dj_rest_auth.urls')), #login, logout and password change
        path('api/v1/rest-auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(),name='account_confirm_email'),
        path(api_version+'rest-auth/registration/', include('dj_rest_auth.registration.urls')),#registration
        path('api/v1/otp-auth/', include('drfpasswordless.urls')),

        ##Password-reset
        path('api/v1/rest-auth/password/reset/<uidb64>/<token>/', \
                auth_views.PasswordResetConfirmView.as_view(),  \
                name='password_reset_confirm'),
        path('api/v1/rest-auth/password-reset-complete/',
                auth_views.PasswordResetCompleteView.as_view(),
                name='password_reset_complete'),
]
