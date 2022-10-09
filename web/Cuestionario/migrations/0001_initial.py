# Generated by Django 4.1 on 2022-09-27 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Test", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Informacion",
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
                ("desc", models.CharField(max_length=600)),
                ("url_radiopaedia", models.URLField(blank=True)),
                ("url_SERAM", models.URLField(blank=True)),
                (
                    "resp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Test.alternativa",
                    ),
                ),
            ],
        ),
    ]
