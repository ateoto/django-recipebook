from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from recipebook.models import RecipeIngredient, Ingredient, Recipe, IngredientLine


class RecipeTestCase(TestCase):
		def setUp(self):
			self.water = Ingredient.objects.create(name='Water')
			self.salt = Ingredient.objects.create(name='Salt')
			self.yeast = Ingredient.objects.create(name='Instant yeast')
			self.bf = Ingredient.objects.create(name='Bread flour')
			self.apf = Ingredient.objects.create(name='All purpose flour')

		def test_recipe_create(self):
			recipe = Recipe.objects.create(name='Pate Fermente', method='Mix and rest')
			ingredient_ct = ContentType.objects.get_for_model(Ingredient)
			
			ri_water = RecipeIngredient.objects.get(
				content_type__pk=ingredient_ct.id,
				object_id=self.water.id
			)
			ri_salt = RecipeIngredient.objects.get(
				content_type__pk=ingredient_ct.id,
				object_id=self.salt.id
			)
			water = IngredientLine.objects.create(
				recipe=recipe, 
				ingredient=ri_water, 
				amount='6 ounces'
			)
			salt = IngredientLine.objects.create(
				recipe=recipe,
				ingredient=ri_salt,
				amount='2 grams'
			)
			self.assertIn(water.ingredient, recipe.ingredients.all())
			self.assertIn(salt.ingredient, recipe.ingredients.all())