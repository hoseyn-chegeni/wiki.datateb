# Generated by Django 5.0.6 on 2024-05-18 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_remove_article_images_article_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]