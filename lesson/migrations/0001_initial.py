# Generated by Django 4.0.4 on 2024-02-23 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='Превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('link_to_video', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
