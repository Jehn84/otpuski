# Generated by Django 2.1.3 on 2019-05-17 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacation',
            name='fio',
        ),
        migrations.AddField(
            model_name='vacation',
            name='employee',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Employee'),
            preserve_default=False,
        ),
    ]
