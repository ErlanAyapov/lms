# Generated by Django 4.2.1 on 2023-05-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_feedback_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='comment',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Номер телефона'),
        ),
    ]
