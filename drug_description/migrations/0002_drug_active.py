# Generated by Django 4.2.5 on 2023-09-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug_description', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
