from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
