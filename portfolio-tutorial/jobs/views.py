from django.shortcuts import render

# Create your views here.
def shouyi(request):
    return render(request, 'jobs/shouyi.html')

def home(request):
    return render(request, 'jobs/home.html')