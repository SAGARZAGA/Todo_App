# Generated by Django 3.2.14 on 2022-07-27 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-12-12'),
            preserve_default=False,
        ),
    ]
