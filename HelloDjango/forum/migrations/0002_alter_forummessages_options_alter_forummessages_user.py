# Generated by Django 4.1.4 on 2022-12-22 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forummessages',
            options={'verbose_name': 'Сообщения форума'},
        ),
        migrations.AlterField(
            model_name='forummessages',
            name='user',
            field=models.TextField(),
        ),
    ]