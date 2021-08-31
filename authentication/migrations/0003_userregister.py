# Generated by Django 3.2.6 on 2021-08-30 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20210828_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password2', models.CharField(max_length=200)),
            ],
        ),
    ]