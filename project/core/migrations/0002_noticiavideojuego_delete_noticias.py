# Generated by Django 4.2.7 on 2023-12-24 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticiaVideojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='noticias',
        ),
    ]
