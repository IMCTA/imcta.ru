# Generated by Django 3.1.12 on 2021-07-15 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='frontpage',
            old_name='about_header_zh_cn',
            new_name='about_header_zh_hans',
        ),
        migrations.RenameField(
            model_name='frontpage',
            old_name='about_text_zh_cn',
            new_name='about_text_zh_hans',
        ),
        migrations.RenameField(
            model_name='frontpage',
            old_name='hero_header_zh_cn',
            new_name='hero_header_zh_hans',
        ),
        migrations.RenameField(
            model_name='frontpage',
            old_name='hero_text_zh_cn',
            new_name='hero_text_zh_hans',
        ),
        migrations.RenameField(
            model_name='frontpage',
            old_name='more_info_header_zh_cn',
            new_name='more_info_header_zh_hans',
        ),
        migrations.RenameField(
            model_name='frontpage',
            old_name='more_info_text_zh_cn',
            new_name='more_info_text_zh_hans',
        ),
        migrations.RenameField(
            model_name='frontpage',
            old_name='why_us_header_zh_cn',
            new_name='why_us_header_zh_hans',
        ),
        migrations.RenameField(
            model_name='frontpage',
            old_name='why_us_text_zh_cn',
            new_name='why_us_text_zh_hans',
        ),
    ]
