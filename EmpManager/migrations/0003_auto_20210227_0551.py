# Generated by Django 3.1.7 on 2021-02-27 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmpManager', '0002_auto_20210227_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='EmpManager.employee'),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
