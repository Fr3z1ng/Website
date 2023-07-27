# Generated by Django 4.2 on 2023-05-04 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0011_remove_photogallery_short_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="first_name",
            field=models.CharField(max_length=25, verbose_name="Имя пользователя"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="last_name",
            field=models.CharField(max_length=25, verbose_name="Фамилия пользователя"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(
                max_length=20, verbose_name="Номер телефона пользователя"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="description",
            field=models.TextField(max_length=1000, verbose_name="Описание услуги"),
        ),
        migrations.AlterField(
            model_name="service",
            name="minuses",
            field=models.TextField(max_length=1000, verbose_name="Описание минусов"),
        ),
        migrations.AlterField(
            model_name="service",
            name="name",
            field=models.CharField(max_length=50, verbose_name="Название услуги"),
        ),
        migrations.AlterField(
            model_name="service",
            name="pros",
            field=models.TextField(max_length=1000, verbose_name="Описание плюсов"),
        ),
        migrations.AlterField(
            model_name="service",
            name="short_description",
            field=models.TextField(max_length=250, verbose_name="Короткое описание"),
        ),
        migrations.AlterField(
            model_name="service",
            name="time",
            field=models.CharField(
                default="15 минут", max_length=40, verbose_name="Длительность услуги"
            ),
        ),
        migrations.AddIndex(
            model_name="photogallery",
            index=models.Index(
                fields=["photo_gallery"], name="website_photo_gallery-index"
            ),
        ),
    ]