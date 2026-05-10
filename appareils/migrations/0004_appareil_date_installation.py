

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appareils', '0003_remove_appareil_date_installation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appareil',
            name='date_installation',
            field=models.DateField(blank=True, null=True),
        ),
    ]
