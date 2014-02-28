# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('ingredient_ptr', models.OneToOneField(serialize=False, to='recipebook.Ingredient', to_field='id', auto_created=True, primary_key=True)),
                ('method', models.TextField()),
            ],
            options={
            },
            bases=('recipebook.ingredient',),
        ),
        migrations.CreateModel(
            name='IngredientLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('recipe', models.ForeignKey(to='recipebook.Recipe', to_field='ingredient_ptr')),
                ('ingredient', models.ForeignKey(to='recipebook.Ingredient', to_field='id')),
                ('amount', models.CharField(max_length=20)),
                ('preparation', models.CharField(blank=True, null=True, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
