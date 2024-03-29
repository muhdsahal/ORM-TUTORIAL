# Generated by Django 4.2.1 on 2023-06-30 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_bck100'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cou_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
                ('person_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.phone')),
                ('skill_name', models.ManyToManyField(to='myapp.skill')),
            ],
        ),
    ]
