# Generated by Django 3.2.12 on 2022-02-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iplmatcheswondata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('teamname', models.CharField(max_length=40, unique=True)),
                ('teamabbr', models.CharField(max_length=5, unique=True)),
                ('matcheswon', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='ipldata',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
