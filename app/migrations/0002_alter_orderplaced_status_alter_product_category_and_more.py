# Generated by Django 4.1.1 on 2024-09-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('H', 'Headphones'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('WTW', 'Women Top Wear'), ('WBW', 'Women Bottom Wear'), ('MC', 'Men Cosmetics'), ('WC', 'Women Cosmetics'), ('MW', 'Mens Watches'), ('WW', 'Womens Watches')], max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='producting'),
        ),
    ]
