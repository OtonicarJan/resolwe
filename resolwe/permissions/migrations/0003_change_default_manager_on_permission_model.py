# Generated by Django 3.1.7 on 2021-11-04 11:13

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("permissions", "0002_migrate_old_permissions"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="permissionmodel",
            managers=[
                ("all_objects", django.db.models.manager.Manager()),
            ],
        ),
    ]
