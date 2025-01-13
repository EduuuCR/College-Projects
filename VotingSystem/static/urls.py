from django.urls import path
from . import views

urlpatterns = [
    path('', views.competition_list, name='competition_list'),
    path('competition/<int:competition_id>/', views.competition_detail, name='competition_detail'),
    path('competition/<int:competition_id>/add-entry/', views.add_entry, name='add_entry'),
    path('entry/<int:entry_id>/vote/', views.vote_entry, name='vote_entry'),
]
