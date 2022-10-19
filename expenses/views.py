from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'expenses/index.html')

def addexpense(request):
    return render(request, 'expenses/addexpense.html')