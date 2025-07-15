from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('mark_downloaded/', views.mark_downloaded, name='mark_downloaded'),
    path('clear_history/', views.clear_history, name='clear_history'),
] 