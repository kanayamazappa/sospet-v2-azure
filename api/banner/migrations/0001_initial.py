# Generated by Django 3.2.9 on 2021-11-08 18:54

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Título do banner', max_length=100, verbose_name='Título')),
                ('banner', imagekit.models.fields.ProcessedImageField(help_text='Imagem do banner da home', upload_to='banners', verbose_name='Banner')),
                ('sort_order', models.PositiveIntegerField(default=0, verbose_name='Ordem')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('link', models.URLField(blank=True, verbose_name='Link')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('sort_order',),
            },
        ),
    ]
