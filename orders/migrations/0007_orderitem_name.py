# Generated by Django 3.1.1 on 2020-10-06 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_orderitem_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='name',
            field=models.CharField(db_index=True, default='Afternoon', max_length=200),
        ),
    ]
