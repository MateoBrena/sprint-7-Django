# Generated by Django 4.2.7 on 2023-11-14 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='tipo_id',
            new_name='tipo',
        ),
    ]