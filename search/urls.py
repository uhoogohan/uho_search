from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('upload', views.UploadView.as_view(), name='upload'),
    path('api/', views.MeiboListCreate.as_view()),
]
