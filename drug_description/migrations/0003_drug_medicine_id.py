# Generated by Django 4.2.5 on 2023-09-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug_description', '0002_drug_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='medicine_id',
            field=models.IntegerField(default=0),
        ),
    ]
