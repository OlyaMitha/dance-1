# Generated by Django 4.0.4 on 2022-05-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direction',
            name='about',
            field=models.CharField(max_length=500),
        ),
    ]