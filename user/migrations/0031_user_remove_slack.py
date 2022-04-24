# Generated by Django 3.1.13 on 2022-04-24 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0030_user_is_forgotten"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="slack_display_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="slack_id",
        ),
        migrations.RemoveField(
            model_name="user",
            name="slack_picture",
        ),
        migrations.RemoveField(
            model_name="user",
            name="slack_picture_hash",
        ),
        migrations.RemoveField(
            model_name="user",
            name="slack_scopes",
        ),
        migrations.RemoveField(
            model_name="user",
            name="slack_status_emoji",
        ),
        migrations.RemoveField(
            model_name="user",
            name="slack_status_text",
        ),
        migrations.RemoveField(
            model_name="user",
            name="slack_token",
        ),
        migrations.AlterField(
            model_name="user",
            name="graduation_year",
            field=models.PositiveIntegerField(blank=True, default=2022, null=True),
        ),
    ]
