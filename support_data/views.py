from .models  import Support
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'support_data/home.html')

def upload(request):
    if request.method == 'GET':
        return render(request, 'support_data/upload.html')
    if request.method == 'POST':
        image = request.FILES.get('image','')
        team_name = request.user
        my_image = Support.objects.create(image=image, team_name=team_name)
        my_image.save()
        return redirect('/home')

def result(request):
    # my_apply = Support.objects.get(id=id)
    return render(request, 'support_data/result.html')
