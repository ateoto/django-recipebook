# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientline',
            name='preparation',
            field=models.CharField(blank=True, max_length=40, null=True),
            preserve_default=True,
        ),
    ]
