from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('dashboard', views.dashboard, name='dashboard'),

    path('create-project', views.create_project, name='create_project'),
    path('project-detail/<str:project_name>/', views.project_detail, name='project_detail'),
    path('change-project/<str:project_name>/', views.project_change, name='project_change'),

    path('manage-tasks/<str:project_name>/', views.project_tasks_page, name='project_tasks_page'),
    path('change-task/<str:taskproject>/<int:taskid>', views.change_task, name='change_task'),

    path('sign-up', views.sign_up, name='sign_up'),

    path('teams', views.teams, name='teams'),
    path('create-team', views.create_team, name='create_team'),
    path('change-members/<str:team_name>', views.change_members_team, name='change_members_team'),
    path('change-team/<str:team_name>', views.change_team_information, name='change_team_information')
]