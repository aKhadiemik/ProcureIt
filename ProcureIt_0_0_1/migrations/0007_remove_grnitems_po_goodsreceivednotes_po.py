# Generated by Django 4.2.7 on 2023-11-09 06:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ProcureIt_0_0_1', '0006_rename_vendor_vendors_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grnitems',
            name='po',
        ),
        migrations.AddField(
            model_name='goodsreceivednotes',
            name='po',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='ProcureIt_0_0_1.purchaseorders'),
            preserve_default=False,
        ),
    ]