from django.urls import path
from .views import LoginView, LogoutView, SignUpView, ForgotPassword, NewPasswordPage, SendOTPView, VerifyOTPView

app_name = 'user'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('forgot_password/', ForgotPassword, name='forgot_password'),
    path('new_passwordpage/<str:email>/', NewPasswordPage, name='new_password'),

    path("phone-login/", SendOTPView.as_view(), name="phone-login"),
    path("verify-otp/", VerifyOTPView.as_view(), name="verify-otp"),

]