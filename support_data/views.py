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
        return redirect(f'/result/{my_image.id}/')

def result(request, id):
    if request.method == 'GET':
        # 업로드 페이지에서 저장한 내용들을 모두 받아와준다.
        my_image = Support.objects.get(id=id)
        return render(request, 'support_data/result.html', {'my_image':my_image})
