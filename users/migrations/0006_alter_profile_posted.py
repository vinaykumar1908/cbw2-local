# Generated by Django 3.2.6 on 2021-11-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Posted',
            field=models.CharField(blank=True, choices=[('TKD Sickline Office', 'TKD Sickline Office'), ('TKD ROH Office', 'TKD ROH'), ('TKD Contract Office', 'TKD Contract Office'), ('TKD Tech Cell Office', 'TKD Tech Cell Office'), ('TKD OMRS Office', 'TKD OMRS Office'), ('TKD SSE Planning Office', 'TKD SSE Planning Office'), ('TKD M&P Section', 'TKD M&P Section'), ('TKD Administration', 'TKD Administration'), ('TKD Stores', 'TKD Stores'), ('TKD Wheel Lathe', 'TKD Wheel Lathe'), ('TKD Train Duty Office', 'TKD Train Duty Office'), ('TKD ICD', 'TKD ICD'), ('DLI DIV', 'DLI DIV'), ('SSB', 'SSB'), ('PNP', 'PNP'), ('GZB', 'GZB')], default='TKD Tech Cell Office', max_length=30, null=True),
        ),
    ]
