# Generated by Django 3.2.12 on 2022-02-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_ipltopeconomicalbowlers_economy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iplextrarunsconcededperseason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('year', models.IntegerField()),
                ('extras', models.IntegerField()),
            ],
        ),
    ]
