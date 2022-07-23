# Generated by Django 4.0.4 on 2022-05-16 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_dance', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainer', models.CharField(max_length=30)),
                ('subscription', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('directions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_app.direction')),
            ],
        ),
    ]