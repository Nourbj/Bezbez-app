# Generated by Django 5.0.2 on 2024-05-07 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_remove_category_main_category_delete_maincategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
