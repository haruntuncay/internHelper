# Generated by Django 2.1.3 on 2018-11-29 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0002_application_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_negative',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]