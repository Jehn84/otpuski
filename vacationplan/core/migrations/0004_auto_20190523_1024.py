# Generated by Django 2.1.3 on 2019-05-23 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_vacation_vsc_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacation',
            old_name='vsc_status',
            new_name='vac_status',
        ),
    ]
