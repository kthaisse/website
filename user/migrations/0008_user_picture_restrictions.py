# Generated by Django 2.2.10 on 2020-03-15 09:05

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [("user", "0007_user_description")]

    operations = [
        migrations.RemoveField(model_name="user", name="picture_public_participants"),
        migrations.RemoveField(
            model_name="user", name="picture_public_sponsors_and_recruiters"
        ),
        migrations.AlterField(
            model_name="user",
            name="picture",
            field=versatileimagefield.fields.VersatileImageField(
                default="user/picture/profile.png",
                upload_to="user/picture/",
                verbose_name="Image",
            ),
        ),
    ]
