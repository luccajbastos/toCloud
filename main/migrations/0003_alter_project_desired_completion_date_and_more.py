# Generated by Django 4.2.6 on 2023-10-28 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_team_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='desired_completion_date',
            field=models.DateTimeField(verbose_name='Prazo de conclusão desejado'),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(verbose_name='Data de início estimada'),
        ),
    ]
