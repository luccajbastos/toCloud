from django.shortcuts import render, redirect
from .forms import RegisterForm, ProjectForm, TeamForm, TaskProjectForm, SubtaskProjectForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .models import UserInformation, Project, Team, ProjectTask, ProjectSubTask
from django.contrib.auth.models import User
from pprint import pprint

# Create your views here.


@login_required(login_url="/login")
def main(request):

    # projects = Project.objects.all()
    # user = User.objects.filter(id=request.user.id).first()
    # teams = Team.objects.filter(members=user).values_list("name", flat=True)
    
    # print (user)
    # context = {
    #     "projects": projects,
    #     "teams": teams
    # }

    return redirect('/dashboard')

@login_required(login_url="/login")
def dashboard(request):
    project = Project.objects.all()
    user = User.objects.filter(id=request.user.id).first()
    user_teams = Team.objects.filter(members=user)
    
    context = {
        "project": project,
        "user_teams": user_teams
    }

    return render(request, 'main/dashboard.html', context)

@login_required(login_url="/login")
def teams(request):
    team = Team.objects.all()
    user = User.objects.filter(id=request.user.id)

    if request.method == "POST":
        team_name = request.POST.get("team-name")
        team = Team.objects.filter(name=team_name).first()
        if team:
            team.delete()
            return redirect('/teams')

    context = {
        "team": team
    }

    return render(request, 'team/teams.html', context)

@login_required(login_url="/login")
def create_team(request):
    if(request.method) == 'POST':
        form = TeamForm(request.POST)
        print(request.user.teams)                                                                                    
        if form.is_valid():
            team = form.save(commit=False)
            team.author = request.user
            team.save()
            return redirect('/teams')
    else:
        form = TeamForm()

    return render(request, 'team/create_team.html', {"form": form})

@login_required(login_url="/login")
def change_members_team(request, team_name):
    team = Team.objects.get(name=team_name)
    members = User.objects.all()

    if request.method == 'POST':
        selected_member_ids = request.POST.getlist('members')

        for member in team.members.all():
            if str(member.id) not in selected_member_ids:
                team.members.remove(member)

        selected_members = User.objects.filter(pk__in=selected_member_ids)
        team.members.add(*selected_members)
        return redirect('/teams')

    context = {
        "team": team,
        "members": members
    }

    return render(request, 'team/manage_users_team.html', context)


@login_required(login_url="/login")
def change_team_information(request, team_name):

    team = Team.objects.filter(name=team_name).first()

    if request.method == "POST":
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('/teams')
    else:
        form = TeamForm(instance=team)

    return render(request, 'team/manage_team_info.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

@login_required(login_url="/login")
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect("/dashboard")
    else:
        form = ProjectForm()

    return render(request, 'project/create_project.html', {"form": form})

@login_required(login_url="/login")
def project_detail(request, project_name):
    project = Project.objects.filter(project_name=project_name).first()
    tasks = ProjectTask.objects.filter(task_project=project)
    user = User.objects.filter(id=request.user.id).first()
    user_teams = Team.objects.filter(members=user)

    if request.method == "POST":
        submit_type = request.POST.get('submit_type')
        if submit_type == 'submitTask':
            form = TaskProjectForm(request.POST)
            if form.is_valid():             
                form.save()
                return redirect(request.META.get('HTTP_REFERER'))

        else:
            projectname = request.POST.get("project-name")
            project = Project.objects.filter(project_name=project_name).first()
            if Project:
                project.delete()
                return redirect(request.META.get('HTTP_REFERER'))

    else:
        form = TaskProjectForm(initial={'task_project':project})

    
    context = {
        "project": project,
        "form": form,
        "tasks": tasks,
        "user_teams": user_teams
    }

    return render(request, 'project/project_detail.html', context)

@login_required(login_url="/login")
def project_change(request, project_name):

    project = Project.objects.filter(project_name=project_name).first()

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = ProjectForm(instance=project)
    
    return render(request, 'project/change_project.html', {"form": form})


@login_required(login_url="/login")
def project_tasks_page(request, project_name):
    
    project = Project.objects.filter(project_name=project_name).first()
    tasks = ProjectTask.objects.filter(task_project=project)
    user = User.objects.filter(id=request.user.id).first()
    teams = Team.objects.filter(members=user)
    form = TaskProjectForm(initial={'task_project':project})

    if request.method == "POST":
        submit_type = request.POST.get('submit_type')
        if submit_type == 'submitTask':
            form = TaskProjectForm(request.POST)
            if form.is_valid():             
                form.save()
                return redirect(request.META.get('HTTP_REFERER'))

        else:
            t_name = request.POST.get("task-name")
            print(t_name)
            task = ProjectTask.objects.filter(task_name=t_name).first()
            if ProjectTask:
                task.delete()
                return redirect(request.META.get('HTTP_REFERER'))
        
    else:
        form = TaskProjectForm(initial={'task_project':project})

    context = {
        "tasks": tasks,
        "project": project,
        "user": user,
        "teams": teams,
        "form": form,
    }

    return render(request, 'tasks/manage_tasks.html', context)


def change_task(request, taskproject, taskid):
    project = Project.objects.filter(project_name=taskproject).first()
    task = ProjectTask.objects.filter(task_project=project, id=taskid).first()

    if request.method == "POST":
        form = TaskProjectForm(request.POST, instance=task)
        print(form)
        if form.is_valid():             
            form.save()
            return redirect(f'/manage-tasks/{project.project_name}')
    else:
        form = TaskProjectForm(instance=task)

    context = {
        "form": form
    }

    return render(request, 'tasks/change_task.html', context)







