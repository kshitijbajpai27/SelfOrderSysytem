# Generated by Django 3.0.5 on 2021-06-24 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_menuitem_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='zip_code',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='state',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='street',
        ),
    ]