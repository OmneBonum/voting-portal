# Generated by Django 4.0.1 on 2022-02-01 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0014_elect_count_elect_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elect_count',
            name='Elect_count',
            field=models.IntegerField(default=1),
        ),
    ]