# Generated by Django 2.0 on 2020-11-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=800)),
                ('creator', models.CharField(max_length=800)),
                ('description', models.TextField(max_length=5000)),
                ('last_updated_date', models.DateField()),
                ('average_rating', models.FloatField()),
            ],
        ),
    ]
