from django.db import models
from django.contrib.contenttypes.models import ContentType
try:
	from django.contrib.contenttypes.fields import GenericForeignKey
except ImportError:
	from django.contrib.contenttypes.generic import GenericForeignKey


class RecipeIngredient(models.Model):
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey()

	def __str__(self):
		return str(self.content_object)

class Ingredient(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % self.name

	def save(self, *args, **kwargs):
		super(Ingredient, self).save(*args, **kwargs)
		RecipeIngredient(content_object=self).save()

class Recipe(models.Model):
	name = models.CharField(max_length=100)
	method = models.TextField()
	ingredients = models.ManyToManyField(RecipeIngredient, through='IngredientLine')

	def __str__(self):
		return '%s' % self.name

	def save(self, *args, **kwargs):
		super(Recipe, self).save(*args, **kwargs)
		RecipeIngredient(content_object=self).save()

class IngredientLine(models.Model):
	recipe = models.ForeignKey(Recipe)
	ingredient = models.ForeignKey(RecipeIngredient)
	amount = models.CharField(max_length=30)