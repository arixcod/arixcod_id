# Generated by Django 4.2.2 on 2023-07-04 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('id_card', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fire_user',
            name='paswword',
        ),
    ]
