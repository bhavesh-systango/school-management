# Generated by Django 4.0 on 2022-07-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'student'), (2, 'teacher'), (3, 'admin')]),
        ),
    ]
