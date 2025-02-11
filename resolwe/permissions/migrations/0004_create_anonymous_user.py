# Generated by Django 3.1.7 on 2021-11-04 11:13

from django.conf import settings
from django.db import migrations


def create_anonymous_user(apps, schema_editor):
    """Create anonymous user if it does not exist."""
    apps.get_model("auth", "User").objects.get_or_create(
        username=settings.ANONYMOUS_USER_NAME
    )


class Migration(migrations.Migration):

    dependencies = [
        ("permissions", "0003_change_default_manager_on_permission_model"),
    ]

    operations = [
        migrations.RunPython(
            create_anonymous_user, reverse_code=migrations.RunPython.noop
        ),
    ]
