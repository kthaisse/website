# Generated by Django 3.1.7 on 2021-05-10 15:20

from django.db import migrations, models
import django.db.models.deletion
import event.enums
import uuid


class Migration(migrations.Migration):

    dependencies = [("event", "0023_speaker")]

    operations = [
        migrations.CreateModel(
            name="SpeakerRole",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "type",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "SPEAKER"), (1, "MODERATOR"), (2, "SPECTATOR")],
                        default=event.enums.SpeakerRoleType["SPEAKER"],
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="roles",
                        to="event.session",
                    ),
                ),
                (
                    "speaker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="roles",
                        to="event.speaker",
                    ),
                ),
            ],
        )
    ]
