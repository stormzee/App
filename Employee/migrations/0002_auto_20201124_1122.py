# Generated by Django 3.1.3 on 2020-11-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.DurationField(default=None, null=True),
        ),
    ]
