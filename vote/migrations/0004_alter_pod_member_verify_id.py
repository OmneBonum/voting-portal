# Generated by Django 4.0.1 on 2022-01-25 10:12

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0003_pod_member_verify_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pod_member',
            name='verify_id',
            field=models.CharField(max_length=200, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]