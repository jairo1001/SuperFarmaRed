

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
