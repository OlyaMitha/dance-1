# Generated by Django 4.0.4 on 2022-06-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0007_lesson_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=models.ImageField(default='static/project_app/images/default.jpg', upload_to='project_app/images/'),
        ),
    ]