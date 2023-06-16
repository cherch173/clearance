from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cases/', views.cases_index, name='index'),
    path('cases/<int:case_id>/', views.cases_detail, name='detail'),
]