# Generated by Django 3.0.5 on 2020-08-14 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='username',
        ),
    ]
