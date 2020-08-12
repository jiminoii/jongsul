from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_food_point_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_point',
            name='tel',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
