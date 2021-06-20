from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('download_as_excel/',views.Download_as_excel, name="Download_as_excel"),
    path('Download_as_PDF/', views.Download_as_PDF, name="Download_as_PDF")
]
