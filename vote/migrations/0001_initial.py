# Generated by Django 4.0.1 on 2022-01-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usersignup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('district', models.CharField(max_length=200)),
                ('voterid', models.IntegerField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('confirmation', models.CharField(max_length=20)),
            ],
        ),
    ]
