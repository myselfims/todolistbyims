# Generated by Django 4.0.5 on 2022-08-04 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_task_task_alter_task_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='task',
            name='username',
            field=models.CharField(default='', max_length=500),
        ),
    ]
