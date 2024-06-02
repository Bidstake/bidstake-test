# Generated by Django 5.0.3 on 2024-04-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlist',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='auctionlist',
            name='image_url',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='auctionlist',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='auctionlist',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='auctionlist',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
