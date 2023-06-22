# Generated by Django 4.2.1 on 2023-06-22 11:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0005_alter_course_students_alter_course_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='student', to=settings.AUTH_USER_MODEL, verbose_name='Студенты'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(related_name='teacher', to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель'),
        ),
    ]
