# Generated by Django 4.1 on 2022-09-27 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Test", "0003_pregunta_img_patologia"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="puntaje_usuario",
            name="pregunta",
        ),
        migrations.AddField(
            model_name="puntaje_usuario",
            name="resp",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Test.alternativa",
            ),
        ),
        migrations.AlterField(
            model_name="alternativa",
            name="resp",
            field=models.CharField(blank=True, max_length=600),
        ),
    ]
