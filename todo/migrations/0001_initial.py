# Generated by Django 4.0.5 on 2022-07-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(default='', max_length=500)),
                ('task', models.CharField(default='', max_length=5000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=500)),
                ('email', models.CharField(default='', max_length=500)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
