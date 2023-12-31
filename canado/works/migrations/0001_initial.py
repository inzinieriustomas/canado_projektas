# Generated by Django 4.2.4 on 2023-08-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pareigos', models.CharField(blank=True, choices=[('dazytojas', 'dazytojas'), ('mechanikas', 'mechanikas'), ('elektrikas', 'elektrikas'), ('saltkalvis', 'saltkalvis'), ('vadybininkas', 'vadybininkas')], max_length=20)),
                ('darbas', models.CharField(max_length=254)),
                ('category', models.CharField(default='-', max_length=256, verbose_name='Kategorija')),
                ('c_remarks', models.CharField(default='-', max_length=256, verbose_name='Pastabos')),
                ('start_time', models.DateTimeField(verbose_name='Darbo pradžios laikas')),
                ('end_time', models.DateTimeField(verbose_name='Darbo pabaigos laikas')),
            ],
        ),
    ]
