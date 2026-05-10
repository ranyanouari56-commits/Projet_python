

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('releves', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='releve',
            name='puissance_instantanee',
        ),
    ]
