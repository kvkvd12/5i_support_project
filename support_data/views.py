from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'support_data/home.html')

def upload(request):
    if request.method == 'GET':
        return render(request, 'support_data/upload.html')
    # if request.method == 'POST':

