from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
# Create your views here.
class UsernameValidateView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should be alphanumeric'}, status=400)
        if len(username) < 5:
            return JsonResponse({'username_error': 'username should be more than 5 letters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'USER_EXISTS'}, status=400)
        
        
        return JsonResponse({'username_valid': 'username is valid'}, status=200)

class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')