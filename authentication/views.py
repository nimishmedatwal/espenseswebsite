from email.errors import MessageError
from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
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
class EmailValidateView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'email is invalid'}, status=400)
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'email already exists'}, status=400)
        
        return JsonResponse({'email_valid': 'email is valid'}, status=200)

class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    def post(self, request):
        messages.success(request, 'Registration successful')
        messages.warning(request, 'hello')
        messages.info(request, 'Registration info')
        messages.error(request, 'Registration not successful')
        return render(request, 'authentication/register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')