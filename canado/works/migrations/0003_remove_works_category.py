# Generated by Django 4.2.4 on 2023-09-01 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_works_valandinis_ikainis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='works',
            name='category',
        ),
    ]