# Generated by Django 4.2.1 on 2023-05-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercustomer',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/user/', verbose_name='Изоброжение'),
        ),
    ]
