# Generated by Django 4.1.7 on 2023-03-13 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('s_name', models.CharField(max_length=111)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('data_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]