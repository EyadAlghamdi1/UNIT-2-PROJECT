# Generated by Django 5.1.2 on 2024-11-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_github_url_project_live_url_project_tools'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]