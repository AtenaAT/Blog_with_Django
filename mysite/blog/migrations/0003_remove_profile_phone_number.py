# Generated by Django 4.1 on 2022-08-23 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]
