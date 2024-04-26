# Generated by Django 4.2.9 on 2024-04-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Lists", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="tlist", name="city",),
        migrations.RemoveField(model_name="tlist", name="likes",),
        migrations.AddField(
            model_name="tlist",
            name="likes_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="tlist",
            name="location",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]