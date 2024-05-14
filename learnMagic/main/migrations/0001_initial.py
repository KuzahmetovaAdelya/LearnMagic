# Generated by Django 5.0.6 on 2024-05-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Имя')),
                ('password', models.CharField(default='', max_length=20, verbose_name='Пароль')),
                ('role', models.CharField(default='0', max_length=10, verbose_name='Роль')),
            ],
        ),
    ]