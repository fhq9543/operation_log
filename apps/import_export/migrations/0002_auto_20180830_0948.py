# Generated by Django 2.0 on 2018-08-30 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_export', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='exportrecord',
            table='export_records',
        ),
        migrations.AlterModelTable(
            name='importrecord',
            table='import_records',
        ),
    ]