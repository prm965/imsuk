# Generated by Django 5.2 on 2025-05-05 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allergen',
            options={'verbose_name_plural': '🍽 เมนูและร้านอาหาร | Allergens'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name_plural': '🛒 ตะกร้าสินค้า | Cart items'},
        ),
        migrations.AlterModelOptions(
            name='menuitem',
            options={'verbose_name_plural': '🍽 เมนูและร้านอาหาร | Menu items'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': '🛒 ตะกร้าสินค้า | Orders'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name_plural': '🛒 ตะกร้าสินค้า | Order items'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'verbose_name_plural': '🍽 เมนูและร้านอาหาร | Restaurants'},
        ),
    ]
