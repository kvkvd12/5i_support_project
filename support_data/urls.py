from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('result/<int:id>/', views.result, name='result'),
    path('my_result/', views.my_result, name='my_result'),
    path('team_result/', views.team_result, name='team_result'),
    path('approval/', views.approval_list, name='approval_list'),
    path('approval/<int:id>/', views.approval, name='approval'),
    path('my_result/', views.my_result, name='my_result'),
    path('error/<int:id>/', views.error, name='error'),
    path('objection_list/', views.objection_list, name='objection_list'),
    # path('objection_list/<int:id>/', views.object, name='objection_list'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)