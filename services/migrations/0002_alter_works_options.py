# Generated by Django 4.1.7 on 2023-03-16 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='works',
            options={'verbose_name': 'Work', 'verbose_name_plural': 'Works'},
        ),
    ]