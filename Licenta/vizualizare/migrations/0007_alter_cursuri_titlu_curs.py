# Generated by Django 4.2.1 on 2023-06-12 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vizualizare', '0006_students_cetatenia_students_mama_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursuri',
            name='titlu_curs',
            field=models.CharField(max_length=100),
        ),
    ]
