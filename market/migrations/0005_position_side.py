# Generated migration to add position side field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_alter_position_options_position_lots_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='side',
            field=models.CharField(
                choices=[('LONG', 'Long'), ('SHORT', 'Short')],
                default='LONG',
                help_text='LONG or SHORT position',
                max_length=10,
                verbose_name='Position Side'
            ),
        ),
    ]
