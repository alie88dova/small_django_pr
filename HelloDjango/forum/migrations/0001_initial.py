# Generated by Django 4.1.4 on 2022-12-19 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForumMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('content', models.TextField(default='Error in base')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
