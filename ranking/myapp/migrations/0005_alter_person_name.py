# Generated by Django 5.0.1 on 2024-01-24 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
