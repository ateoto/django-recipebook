from django.db import models
from django.db.models import Q
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
		if not self.id:
			new = True
		else:
			new = False
		super(Ingredient, self).save(*args, **kwargs)
		if new:
			RecipeIngredient(content_object=self).save()

class Recipe(models.Model):
	name = models.CharField(max_length=100)
	method = models.TextField()
	ingredients = models.ManyToManyField(RecipeIngredient, through='IngredientLine')

	def __str__(self):
		return '%s' % self.name

	def save(self, *args, **kwargs):
		if not self.id:
			new = True
		else:
			new = False
		super(Recipe, self).save(*args, **kwargs)
		if new:
			RecipeIngredient(content_object=self).save()

class IngredientLine(models.Model):
	recipe = models.ForeignKey(Recipe)
	ingredient = models.ForeignKey(RecipeIngredient, limit_choices_to=lambda: Q(content_type=ContentType.objects.get_for_model(Recipe)) | Q(content_type=ContentType.objects.get_for_model(Ingredient)))
	amount = models.CharField(max_length=30)
	preparation = models.CharField(max_length=40, blank=True, null=True)

	def __str__(self):
		if self.preparation:
			prep_str = ' (%s)' % (self.preparation)
		else:
			prep_str = ''
		return '%s %s%s' % (str(self.ingredient), self.amount, prep_str)
