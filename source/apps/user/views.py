from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, self.template_name, {'error': 'Invalid username or password'})
   



# from django.shortcuts import render

# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy

# class UserLoginView(LoginView):
#     template_name = 'login.html'  
#     redirect_authenticated_user = True  
#     success_url = reverse_lazy('index')  

#     def get_success_url(self):
#         return self.success_url




# def login(request):
#     return render(request, 'login.html')


