# Generated by Django 3.1.3 on 2020-12-18 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_download'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Download',
        ),
    ]