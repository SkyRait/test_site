# Generated by Django 4.1.4 on 2022-12-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('point', models.CharField(max_length=250, verbose_name='Point')),
                ('place', models.CharField(max_length=250, verbose_name='Place')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
    ]
