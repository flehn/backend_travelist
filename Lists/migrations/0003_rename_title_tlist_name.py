# Generated by Django 4.2.9 on 2024-01-31 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Lists", "0002_tlist_likes"),
    ]

    operations = [
        migrations.RenameField(model_name="tlist", old_name="title", new_name="name",),
    ]