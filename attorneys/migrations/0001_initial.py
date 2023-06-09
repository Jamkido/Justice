# Generated by Django 4.1.7 on 2023-03-13 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attorneys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=222)),
                ('image', models.ImageField(upload_to='media/images')),
                ('occupation', models.CharField(max_length=222)),
                ('content', models.TextField()),
            ],
        ),
    ]
