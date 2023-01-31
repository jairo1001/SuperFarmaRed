

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0005_auto_20191110_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='total',
        ),
        migrations.AddField(
            model_name='basket',
            name='total_morrisons',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='basket',
            name='total_sainsburys',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='basket',
            name='total_tesco',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
