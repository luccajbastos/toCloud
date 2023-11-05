from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Team, ProjectTask, ProjectSubTask
from django.forms import TextInput, Textarea
import datetime

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True, label="Usuário")
    email = forms.EmailField(required=True, label="E-mail")
    first_name = forms.CharField(required=True, label="Nome")

    class Meta:
        model = User
        fields = ["first_name", "username", "email"]


class TeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Team
        fields = [
            "name",
            "description",
            "members"
        ]

class ProjectForm(forms.ModelForm):
    

    start_date = forms.DateField(initial=datetime.date.today)
    desired_completion_date = forms.DateField(initial='ano/mes/dia')
    budget = forms.FloatField(label='Orçamento do projeto (R$)', initial='1000.00')

    class Meta:
        model = Project
        fields = [
            "project_name",
            "software_objective",
            "features_and_functionality",
            "target_audience",
            "technical_requirements",
            "target_platforms",
            "initial_scope",
            "future_scope",
            "start_date",
            "desired_completion_date",
            "budget",
            "team",
            "additional_notes",
        ]


class TaskProjectForm(forms.ModelForm):

    task_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'Nome da task'}))
    task_description = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'placeholder': 'Descrição da task'}))
    task_done = forms.CheckboxInput()

    class Meta:
        model = ProjectTask
        fields = [
            "task_name",
            "task_description",
            "task_project",
            "task_done"
        ]

class SubtaskProjectForm(forms.ModelForm):

    subtask_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': 'Nome da subtask'}))
    subtask_done = forms.BooleanField(label="", required=False)



    class Meta:
        model = ProjectSubTask
        fields = [
            "subtask_name",
            "subtask_done",
            "subtask_task"
        ]