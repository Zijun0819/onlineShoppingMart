# Generated by Django 5.1.4 on 2024-12-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("df_order", "0002_auto_20181218_1200"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderdetailinfo",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
