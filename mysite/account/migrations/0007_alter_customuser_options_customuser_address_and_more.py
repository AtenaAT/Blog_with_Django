# Generated by Django 4.1 on 2022-08-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_profile_age_alter_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'پروفایل کاربری', 'verbose_name_plural': 'پروفایل کاربری'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name=' آدرس'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(null=True, verbose_name='سن'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'خانم'), ('male', 'آقا')], max_length=10, null=True, verbose_name='جنسیت'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='account/static/images/profile_pictures/default/default.png', null=True, upload_to='blog/static/images/profile_pictures', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='نام خانوادگی'),
        ),
    ]
