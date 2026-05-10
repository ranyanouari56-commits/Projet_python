

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releves', '0002_remove_releve_puissance_instantanee'),
    ]

    operations = [
        migrations.AddField(
            model_name='releve',
            name='puissance_instantanee',
            field=models.FloatField(default=0, help_text='Puissance en Watts au moment du relevé'),
        ),
    ]
