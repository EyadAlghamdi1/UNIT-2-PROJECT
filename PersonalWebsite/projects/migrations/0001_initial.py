# Generated by Django 5.1.2 on 2024-11-12 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('category', models.CharField(choices=[('WebApplication', 'WebApplication'), ('MoblieApplication', 'Moblie Application'), ('SciencePaper', 'Science Paper')], max_length=256)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
