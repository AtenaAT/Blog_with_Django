# Generated by Django 4.1 on 2022-08-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='blog/static/images/profile_pictures/default.png', null=True, upload_to='blog/static/images/profile_pictures', verbose_name='تصویر'),
        ),
    ]