# Generated by Django 4.2.1 on 2023-06-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vizualizare', '0004_alter_note_valoare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='data_notare',
            field=models.DateField(blank=True, null=True),
        ),
    ]