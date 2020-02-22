# Generated by Django 2.2.4 on 2020-02-22 10:57

from django.db import migrations, models
import uuid
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('slug', models.CharField(blank=True, max_length=255, unique=True)),
                ('picture', versatileimagefield.fields.VersatileImageField(upload_to='news/article/', verbose_name='Image')),
                ('body', models.TextField()),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'DRAFT'), (1, 'REVIEWED'), (2, 'PUBLISHED'), (3, 'DELETED')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
