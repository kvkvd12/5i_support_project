from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('result/<int:id>/', views.result, name='result'),
    path('approval/', views.approval_list, name='approval_list'),
    path('approval/<int:id>/', views.approval, name='approval'),
    path('my_result/', views.my_result, name='my_result'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)