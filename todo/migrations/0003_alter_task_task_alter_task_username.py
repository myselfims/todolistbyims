# Generated by Django 4.0.5 on 2022-08-04 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(default='', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='username',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
