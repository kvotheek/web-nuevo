# Generated by Django 4.1 on 2022-09-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Test", "0002_rename_puntaje_usuarios_puntaje_usuario"),
    ]

    operations = [
        migrations.AddField(
            model_name="pregunta",
            name="img_patologia",
            field=models.ImageField(blank=True, upload_to="radiopaedia/imgs/"),
        ),
    ]
