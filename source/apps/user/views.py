from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from apps.user.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
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