# Generated by Django 3.2.5 on 2022-05-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, unique=True, verbose_name='username'),
        ),
    ]
