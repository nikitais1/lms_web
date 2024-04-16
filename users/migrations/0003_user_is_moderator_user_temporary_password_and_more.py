# Generated by Django 5.0.2 on 2024-04-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_moderator',
            field=models.BooleanField(default=False, verbose_name='Модератор?'),
        ),
        migrations.AddField(
            model_name='user',
            name='temporary_password',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Temporary password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Последнее посещение сервиса'),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]