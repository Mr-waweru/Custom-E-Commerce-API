# Generated by Django 5.1.6 on 2025-02-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_category_unique_category_name_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='category',
            name='unique_category_name_case_insensitive',
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='idx_name_lower'),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_category_name'),
        ),
    ]
