# Generated by Django 3.1.12 on 2021-07-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_zh_cn', models.CharField(max_length=255, null=True)),
                ('subtitle', models.CharField(max_length=255)),
                ('subtitle_ru', models.CharField(max_length=255, null=True)),
                ('subtitle_en', models.CharField(max_length=255, null=True)),
                ('subtitle_zh_cn', models.CharField(max_length=255, null=True)),
                ('announcement', models.TextField()),
                ('announcement_ru', models.TextField(null=True)),
                ('announcement_en', models.TextField(null=True)),
                ('announcement_zh_cn', models.TextField(null=True)),
                ('date', models.DateField()),
                ('event_program', models.TextField()),
                ('event_program_ru', models.TextField(null=True)),
                ('event_program_en', models.TextField(null=True)),
                ('event_program_zh_cn', models.TextField(null=True)),
                ('thumbnail', models.ImageField(blank=True, upload_to='tours/thumbnails/')),
            ],
        ),
    ]
