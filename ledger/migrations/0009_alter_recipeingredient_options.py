# Generated by Django 5.0.2 on 2024-03-15 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0008_alter_recipe_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipeingredient',
            options={'ordering': ['ingredient']},
        ),
    ]