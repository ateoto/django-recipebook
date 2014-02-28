from django.db import models

class Ingredient(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % self.name

class Recipe(Ingredient):
	method = models.TextField()

	def __str__(self):
		return '%s' % str(self.name)

class IngredientLine(models.Model):
	recipe = models.ForeignKey(Recipe, related_name='ingredients')
	ingredient = models.ForeignKey(Ingredient, related_name='+')
	amount = models.CharField(max_length=20)
	preparation = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return '%s for %s' % (self.ingredient.name, self.recipe.name)