# Generated by Django 4.0 on 2021-12-14 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_task_interviewdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='interviewdate',
        ),
    ]
