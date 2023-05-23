from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_add_comment_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
