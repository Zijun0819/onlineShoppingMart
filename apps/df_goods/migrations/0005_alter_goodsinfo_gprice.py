# Generated by Django 5.1.4 on 2024-12-26 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("df_goods", "0004_alter_goodsinfo_gpic_alter_goodsinfo_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="goodsinfo",
            name="gprice",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="商品价格"
            ),
        ),
    ]
