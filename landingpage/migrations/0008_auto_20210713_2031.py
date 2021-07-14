# Generated by Django 3.1.12 on 2021-07-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0007_auto_20210713_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='about_header_cn',
            field=models.CharField(max_length=127, null=True, verbose_name="Заголовок раздела 'О нас''"),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='about_text_cn',
            field=models.TextField(null=True, verbose_name="Текст раздела 'О нас'"),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='hero_header_cn',
            field=models.CharField(max_length=127, null=True, verbose_name='Заголовок слайдера'),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='hero_text_cn',
            field=models.CharField(max_length=255, null=True, verbose_name='Текст слайдера'),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='more_info_header_cn',
            field=models.CharField(blank=True, max_length=127, null=True, verbose_name="Заголовок раздела 'Дополнительно''"),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='more_info_text_cn',
            field=models.TextField(blank=True, null=True, verbose_name="Текст раздела 'Дополнительно'"),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='why_us_header_cn',
            field=models.CharField(max_length=127, null=True, verbose_name="Заголовок раздела 'Почему мы'"),
        ),
        migrations.AddField(
            model_name='landingpage',
            name='why_us_text_cn',
            field=models.TextField(null=True, verbose_name="Текст раздела 'Почему мы'"),
        ),
    ]