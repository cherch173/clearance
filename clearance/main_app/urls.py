from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cases/', views.cases_index, name='index'),
    path('cases/<int:case_id>/', views.cases_detail, name='detail'),
    path('cases/create/', views.CaseCreate.as_view(), name='cases_create'),
    path('cases/<int:pk>/update/', views.CaseUpdate.as_view(), name='cases_update'),
    path('cases/<int:pk>/delete/', views.CaseDelete.as_view(), name='cases_delete'),
    path('cases/<int:case_id>/add_report/', views.add_report, name='add_report'),
    path('cases/<int:case_id>/assoc_testimony/<int:testimony_id>/', views.assoc_testimony, name='assoc_testimony'),
    path('cases/<int:case_id>/create_testimony/', views.TestimonyCreate.as_view(), name='testimonies_create'),
    path('cases/<int:case_id>/<int:pk>/update_testimony/', views.TestimonyUpdate.as_view(), name='testimonies_update'),
    path('cases/<int:case_id>/<int:pk>/delete_testimony/', views.TestimonyDelete.as_view(), name='testimonies_delete')
]