# Generated by Django 4.2.4 on 2023-08-25 02:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Secretory", "0006_alter_secratory_sec_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="secratory",
            name="sec_from",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 8, 25, 2, 23, 18, 186434, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
