# Generated by Django 4.0.1 on 2022-02-01 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0018_pod_member_pod_vote_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pod_member',
            name='pod_vote_given',
        ),
    ]
