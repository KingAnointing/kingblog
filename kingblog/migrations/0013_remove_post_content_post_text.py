# Generated by Django 4.0.3 on 2022-07-06 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kingblog', '0012_remove_post_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
