# Generated by Django 5.1.6 on 2025-04-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Moviename', models.CharField(max_length=100)),
                ('Actor', models.CharField(max_length=100)),
                ('Rating', models.FloatField()),
                ('Releaseyear', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
    ]
