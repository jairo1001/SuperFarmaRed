
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_thumbnail'),
        ('basket', '0003_auto_20191110_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=models.CASCADE, to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='basket',
            name='items',
            field=models.ManyToManyField(blank=True, to='basket.BasketItem'),
        ),
    ]
