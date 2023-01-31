

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191101_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_morrisons',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_sainsburys',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_tesco',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
