# Generated by Django 4.1.13 on 2024-09-11 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0011_alter_comment_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
