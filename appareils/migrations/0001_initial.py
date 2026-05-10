

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_zone', models.CharField(max_length=100)),
                ('limite_puissance', models.FloatField(help_text='Limite de puissance en Watts')),
            ],
            options={
                'verbose_name': 'Zone',
                'verbose_name_plural': 'Zones',
            },
        ),
        migrations.CreateModel(
            name='Appareil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('type_alimentation', models.CharField(choices=[('monophase', 'Monophasé'), ('triphase', 'Triphasé'), ('solaire', 'Solaire'), ('batterie', 'Batterie')], default='monophase', max_length=50)),
                ('puissance_nominale', models.FloatField(help_text='Puissance nominale en Watts')),
                ('date_installation', models.DateField(auto_now_add=True)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appareils', to='appareils.zone')),
            ],
            options={
                'verbose_name': 'Appareil',
                'verbose_name_plural': 'Appareils',
            },
        ),
    ]
