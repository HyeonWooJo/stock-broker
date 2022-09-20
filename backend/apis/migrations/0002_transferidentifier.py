# Generated by Django 4.1.1 on 2022-09-20 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TransferIdentifier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account_number", models.CharField(max_length=100)),
                ("user_name", models.CharField(max_length=100)),
                ("transfer_amount", models.IntegerField(default=0)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="apis.account"
                    ),
                ),
            ],
            options={
                "db_table": "transfer_identifiers",
            },
        ),
    ]
