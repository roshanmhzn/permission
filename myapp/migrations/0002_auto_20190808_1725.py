# Generated by Django 2.2.4 on 2019-08-08 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': (('can_make_flutter_effect', 'Can make flutter effect'),)},
        ),
    ]