from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200)
    author = models.CharField(User, default='admin')
    members = models.ManyToManyField(User, related_name='teams')
    
    def __str__(self):
        return self.name

class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ManyToManyField(Team)


class Project(models.Model):
    # Informações Gerais
    project_name = models.CharField(max_length=200, verbose_name="Nome do projeto", unique=True)
    author = models.CharField(User)

    # Requisitos de Negócios
    software_objective = models.TextField(verbose_name="Descrição do objetivo do software (gestão de projetos)")
    features_and_functionality = models.TextField(verbose_name="Principais recursos e funcionalidades esperadas")
    target_audience = models.CharField(max_length=200, verbose_name="Público-alvo ou segmento de mercado")

    # Tecnologias e Plataformas
    technical_requirements = models.TextField(verbose_name="Requisitos técnicos específicos (por exemplo, Python, Django, banco de dados, etc.)")
    target_platforms = models.CharField(max_length=100, verbose_name="Plataformas alvo (web, dispositivos móveis, etc.)")

    # Escopo do Projeto
    initial_scope = models.TextField(verbose_name="Escopo inicial do projeto")
    future_scope = models.TextField(verbose_name="Recursos que podem ser adicionados em fases posteriores")

    # Prazos e Orçamento
    start_date = models.DateTimeField(verbose_name="Data de início estimada")
    desired_completion_date = models.DateTimeField(verbose_name="Prazo de conclusão desejado")
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Orçamento disponível")

    # Equipe Envolvida
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Time", unique=False)

    # Tarefas
    tasks = models.TextField(verbose_name="Tarefas", null=True)

    # Outras Observações
    additional_notes = models.TextField(verbose_name="Quaisquer informações adicionais que a equipe de desenvolvimento deve saber")

    def __str__(self):
        return self.project_name

class ProjectTask(models.Model):
    task_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    task_done = models.BooleanField(default=False)
    task_name = models.CharField(max_length=30)
    task_description = models.CharField(max_length=200)

class ProjectSubTask(models.Model):
    subtask_name = models.CharField()
    subtask_done = models.BooleanField(default=False)
    subtask_task = models.ForeignKey(ProjectTask, null=False, on_delete=models.CASCADE)

