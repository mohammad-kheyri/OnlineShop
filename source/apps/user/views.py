from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = 'login.html'  
    redirect_authenticated_user = True  
    success_url = reverse_lazy('index')  

    def get_success_url(self):
        return self.success_url



# def login(request):
#     return render(request, 'login.html')


