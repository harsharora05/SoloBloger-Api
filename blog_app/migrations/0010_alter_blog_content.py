# Generated by Django 5.0.6 on 2024-05-29 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_rename_review_comment_rename_content_comment_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=1500),
        ),
    ]