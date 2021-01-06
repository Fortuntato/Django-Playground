from django.shortcuts import render
from .models import Job
# Create your views here.
def shouyi(request):
    return render(request, 'jobs/shouyi.html')

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

