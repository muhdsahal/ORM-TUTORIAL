# Generated by Django 4.2.1 on 2023-06-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_std'),
    ]

    operations = [
        migrations.CreateModel(
            name='bck100',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('domain', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]