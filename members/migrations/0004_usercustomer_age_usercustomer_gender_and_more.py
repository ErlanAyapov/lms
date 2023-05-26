# Generated by Django 4.2.1 on 2023-05-26 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_usercustomer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercustomer',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Возрасть'),
        ),
        migrations.AddField(
            model_name='usercustomer',
            name='gender',
            field=models.CharField(choices=[('Other', 'Other'), ('Man', 'Man'), ('Woman', 'Woman')], default='Other', max_length=7, null=True, verbose_name='Пол'),
        ),
        migrations.AddField(
            model_name='usercustomer',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='uploads/user/resume'),
        ),
        migrations.AlterField(
            model_name='usercustomer',
            name='user_role',
            field=models.CharField(choices=[('Guest', 'Guest'), ('Student', 'Student'), ('Teacher', 'Teacher'), ('Super admin', 'Super admin'), ('Admin', 'Admin')], default='Guest', max_length=15, null=True, verbose_name='Статус пользователья'),
        ),
    ]
