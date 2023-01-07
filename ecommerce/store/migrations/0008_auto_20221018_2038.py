# Generated by Django 3.2.10 on 2022-10-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_sr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_zh_hans',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_sr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_zh_hans',
            field=models.CharField(max_length=200, null=True),
        ),
    ]