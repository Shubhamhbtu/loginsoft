# Generated by Django 3.1.7 on 2021-02-27 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmpManager', '0003_auto_20210227_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='designation',
        ),
    ]
