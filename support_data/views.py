from support_data.machine import transform_image
from .models  import Support
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    if request.method == 'GET':
        my_images = Support.objects.all().order_by('-id')
        return render(request, 'support_data/home.html', {'my_images':my_images})
     

def upload(request):
    if request.method == 'GET':
        return render(request, 'support_data/upload.html')
    if request.method == 'POST':
        image = request.FILES.get('image','')
        team_name = request.user
        input_num = request.POST.get('input_num','')
        my_image = Support.objects.create(image=image, team_name=team_name,input_num=input_num)
        my_image.save()
        # 머신러닝 코드 불러오기
        my_image.people_num = transform_image(my_image.image.url)
        my_image.save()
        if int(input_num) == my_image.people_num:
            return redirect(f'/result/{my_image.id}/')
        else:
            my_image.delete()
            return render(request, 'support_data/upload.html',{'error':'인원 수가 일치하지 않습니다'})


def result(request, id):
    if request.method == 'GET':
        # 업로드 페이지에서 저장한 내용들을 모두 받아와준다.
        my_image = Support.objects.get(id=id)
        return render(request, 'support_data/result.html', {'my_image':my_image})
    
@login_required    
def approval_list(request):
    if request.method == 'GET':
        approval_list = Support.objects.all()
        return render(request, 'support_data/approval.html', {'approval_list': approval_list})

@login_required        
def approval(request, id):
    approval = Support.objects.get(id=id)
    approval.is_approval.save()
    approval.save()
    
    approval=True
    
    return redirect('/approval')
    

# @login_required        
# def approval(request, id):
#     me = request.user
#     approval=approval
#     click = Support.objects.get(id=id)
#     if me in click.approval.all():
#         approval=True
#     else:
#         click.approval.add(request.user)
#     return redirect('/approval')
