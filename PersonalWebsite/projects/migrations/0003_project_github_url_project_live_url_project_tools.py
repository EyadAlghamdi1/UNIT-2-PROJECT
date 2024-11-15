# Generated by Django 5.1.2 on 2024-11-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='live_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='tools',
            field=models.CharField(default='Not specified', max_length=255),
        ),
    ]
