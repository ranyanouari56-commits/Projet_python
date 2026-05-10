

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appareils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Releve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur_kwh', models.FloatField(help_text='Consommation en kWh')),
                ('puissance_instantanee', models.FloatField(help_text='Puissance instantanée en Watts')),
                ('date_heure_releve', models.DateTimeField(default=django.utils.timezone.now)),
                ('appareil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releves', to='appareils.appareil')),
            ],
            options={
                'verbose_name': 'Relevé',
                'verbose_name_plural': 'Relevés',
                'ordering': ['-date_heure_releve'],
            },
        ),
    ]
