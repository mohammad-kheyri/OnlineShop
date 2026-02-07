from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from apps.user.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from base.settings import EMAIL_HOST_USER
from .forms import SignupForm

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product:index')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
   

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['active_page'] = 'login'
        return context

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('product:index')
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_contect_data()
        context['active_page'] = 'login'
        return context
    

class SignUpView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'signup.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your account has been created successfully! You can now log in.")
        return response

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = super().get_context_data()
        context['active_page'] = 'signup'
        return context
    
from base import settings
def ForgotPassword(request):
    if request.method == "POST":
        email = request.POST.get("email")
        print("Email: ", email)

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            print("User Exists")
            send_mail(
                "Reset Your Password",
                f"Current User: {user}! To reset password, click the link:\nhttp://127.0.0.1:8000/new_passwordpage/{user}/",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False
            )
            # send_mail("Reset Your Password : ", f"Current User: {user}! To reset password , click on the given link \n http://127.0.0.1:8000/new_passwordpage/{user}/", EMAIL_HOST_USER, [email], fail_silently=True)
            return HttpResponse("Password Reset link sent to your email")

        return render(request, 'forgot_password.html')
    return render(request, 'forgot_password.html')

 
def NewPasswordPage(request, email):
    userid = User.objects.get(email=email)
    print("UserId: ", userid)
    if request.method == "POST":
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")

        if pass1 == pass2:
            userid.set_password(pass1)
            userid.save()
            return HttpResponse("Password Reset")
            
    return render(request, 'new_password.html')