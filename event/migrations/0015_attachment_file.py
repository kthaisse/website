# Generated by Django 2.2.10 on 2020-05-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_attachment_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='event/attachment/file/'),
        ),
    ]
