# Generated by Django 4.0.1 on 2022-02-01 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0016_rename_count_pod_member_elect_count_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pod',
            old_name='pod_owner_id',
            new_name='pod_owner',
        ),
    ]
