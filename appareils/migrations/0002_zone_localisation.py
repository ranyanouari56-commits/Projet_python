

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appareils', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='localisation',
            field=models.CharField(blank=True, help_text='Localisation géographique dans le bâtiment', max_length=200, null=True),
        ),
    ]
