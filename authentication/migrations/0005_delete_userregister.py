# Generated by Django 3.2.6 on 2021-08-31 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_user_loginuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserRegister',
        ),
    ]