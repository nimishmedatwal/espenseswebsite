from email.errors import MessageError
from django.shortcuts import redirect, render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

class UsernameValidateView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should be alphanumeric'}, status=400)
        if len(username) < 5:
            return JsonResponse({'username_error': 'username should be more than 5 letters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username already exists!'}, status=400)
        
        
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
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        
        context={
            'fieldValues': request.POST
        }
        if not User.objects.filter(username=username).exists():
            # if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    messages.error(request, 'password should be more than 6 characters')
                    return render(request, 'authentication/register.html',context)
                # user = User.objects.create_user(username=username, email=email)
                # user.set_password(password)
                # user.is_active = False
                # user.save()
                domain=get_current_site(request).domain
                link= reverse('activate', kwargs={'uibd64': uidb64, 'token': token})
                email_subject='Activate your account'
                email_body='Hi {user.username} please use this link to verify your account'
                send_mail(
                    email_subject,
                    email_body,
                    'verifydjango1@gmail.com',
                    [email],
                    fail_silently=False,
                )

                messages.success(request, 'Registered successfully')
                return render(request, 'authentication/register.html')

        return render(request, 'authentication/register.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

class VerificationView(View):
    def get(self, request, uidb64, token):
        return redirect('login')