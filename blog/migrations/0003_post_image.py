# Generated by Django 4.2 on 2023-10-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='posts'),
            preserve_default=False,
        ),
    ]