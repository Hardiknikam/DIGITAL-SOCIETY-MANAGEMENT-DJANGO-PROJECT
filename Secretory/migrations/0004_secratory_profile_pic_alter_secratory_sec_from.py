# Generated by Django 4.2.4 on 2023-08-18 03:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Secretory", "0003_alter_secratory_sec_from"),
    ]

    operations = [
        migrations.AddField(
            model_name="secratory",
            name="profile_pic",
            field=models.FileField(default="avtar.png", upload_to="profile"),
        ),
        migrations.AlterField(
            model_name="secratory",
            name="sec_from",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 18, 3, 10, 0, 698835, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
