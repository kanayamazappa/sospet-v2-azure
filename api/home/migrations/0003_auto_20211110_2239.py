# Generated by Django 3.2.9 on 2021-11-11 01:39

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_quemsomos_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quemsomos',
            options={'verbose_name': 'Quem Somos', 'verbose_name_plural': 'Quem Somos'},
        ),
        migrations.AlterField(
            model_name='quemsomos',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
