# Generated by Django 3.1.13 on 2021-11-23 13:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0005_auto_20211106_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteractiveMessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slack_ts', models.CharField(db_index=True, max_length=255)),
                ('event', models.CharField(db_index=True, max_length=255)),
                ('diet', models.CharField(blank=True, max_length=255, null=True)),
                ('diet_other', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
