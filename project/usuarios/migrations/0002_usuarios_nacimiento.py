# Generated by Django 4.2.7 on 2023-12-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
