# Generated by Django 3.0.8 on 2020-12-31 17:34

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201231_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutionclassdetails',
            name='tution_class',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('0', 'Nursery'), ('1', 'One'), ('2', 'Two'), ('3', 'Three'), ('4', 'Four'), ('5', 'Five'), ('6', 'Six'), ('7', 'Seven'), ('8', 'Eight'), ('9', 'Nine'), ('10', 'Ten')], max_length=50, null=True),
        ),
    ]
