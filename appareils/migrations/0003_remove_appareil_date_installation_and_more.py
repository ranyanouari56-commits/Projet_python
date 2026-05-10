
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appareils', '0002_zone_localisation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appareil',
            name='date_installation',
        ),
        migrations.RemoveField(
            model_name='zone',
            name='localisation',
        ),
    ]
