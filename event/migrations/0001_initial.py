# Generated by Django 2.2.4 on 2020-02-22 21:07

from django.db import migrations, models
import event.enums
import uuid
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(blank=True, max_length=31, unique=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'GENERAL'), (2, 'LECTURE'), (3, 'LUNCH'), (4, 'EXTERNAL'), (5, 'OTHER')], default=event.enums.EventType(1))),
                ('picture', versatileimagefield.fields.VersatileImageField(upload_to='event/picture/', verbose_name='Image')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'DRAFT'), (1, 'PUBLISHED'), (2, 'DELETED')], default=event.enums.EventStatus(0))),
                ('location', models.CharField(max_length=255)),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('signup_starts_at', models.DateTimeField(blank=True, null=True)),
                ('signup_ends_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
