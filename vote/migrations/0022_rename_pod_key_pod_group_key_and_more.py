# Generated by Django 4.0.1 on 2022-02-02 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0021_remove_pod_member_verify_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pod',
            old_name='pod_key',
            new_name='group_key',
        ),
        migrations.RenameField(
            model_name='pod',
            old_name='pod_owner',
            new_name='group_owner_id',
        ),
    ]