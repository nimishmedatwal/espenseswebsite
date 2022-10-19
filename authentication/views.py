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
        if len(username) < 5:
            return JsonResponse({'message': 'username should be more than 5 letters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'USER_EXISTS'}, status=400)
        if not str(username).isalnum():
            return JsonResponse({'message': 'username should be alphanumeric'}, status=400)
        
        return JsonResponse({'message': 'username is valid'}, status=200)
class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')