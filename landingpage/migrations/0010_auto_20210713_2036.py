# Generated by Django 3.1.12 on 2021-07-13 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0009_auto_20210713_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landingpage',
            old_name='about_header_zh_CN',
            new_name='about_header_cn',
        ),
        migrations.RenameField(
            model_name='landingpage',
            old_name='about_text_zh_CN',
            new_name='about_text_cn',
        ),
        migrations.RenameField(
            model_name='landingpage',
            old_name='hero_header_zh_CN',
            new_name='hero_header_cn',
        ),
        migrations.RenameField(
            model_name='landingpage',
            old_name='hero_text_zh_CN',
            new_name='hero_text_cn',
        ),
        migrations.RenameField(
            model_name='landingpage',
            old_name='more_info_header_zh_CN',
            new_name='more_info_header_cn',
        ),
        migrations.RenameField(
            model_name='landingpage',
            old_name='more_info_text_zh_CN',
            new_name='more_info_text_cn',
        ),
        migrations.RenameField(
            model_name='landingpage',
            old_name='why_us_header_zh_CN',
            new_name='why_us_header_cn',
        ),
        migrations.RenameField(
            model_name='landingpage',
            old_name='why_us_text_zh_CN',
            new_name='why_us_text_cn',
        ),
    ]