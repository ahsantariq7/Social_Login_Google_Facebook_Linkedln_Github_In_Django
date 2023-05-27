from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import confirm_email,ConfirmEmailView
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from .views import CustomLoginView,CustomRegisterView,my_view
from dj_rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)


urlpatterns = [
   path('register/', CustomRegisterView.as_view()),
   path('login/', CustomLoginView.as_view()),
   path('logout/', LogoutView.as_view()),
    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
         VerifyEmailView.as_view(), name='account_confirm_email'),
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('password-reset/', PasswordResetView.as_view()),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    path(
        'socialaccounts/',
        SocialAccountListView.as_view(),
        name='social_account_list'
    ),
    path(
        'socialaccounts/<int:pk>/disconnect/',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    ),
   path('my/',my_view)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


