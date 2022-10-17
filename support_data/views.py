from django.shortcuts import render
from .models import Support

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'support_data/home.html')

def upload(request):
    if request.method == 'GET':
        return render(request, 'support_data/upload.html')
    # if request.method == 'POST':

def result(request):
    # my_apply = Support.objects.get(id=id)
    return render(request, 'support_data/result.html')
