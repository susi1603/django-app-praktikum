# Generated by Django 4.0 on 2021-12-12 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task_delete_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='description',
            new_name='descriptions',
        ),
    ]
