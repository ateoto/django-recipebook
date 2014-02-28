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

		def test_recipe_as_ingredient(self):
			pate_fermente = Recipe.objects.create(name='Pate Fermente', method='Mix and rest')
			french_bread = Recipe.objects.create(name='French Bread', method='Be awesome.')
			recipe_ct = ContentType.objects.get_for_model(Recipe)
			ri_pate_fermente = RecipeIngredient.objects.get(
				content_type__pk=recipe_ct.id,
				object_id=pate_fermente.id
			)
			il_pate_fermente = IngredientLine.objects.create(
				recipe=french_bread,
				ingredient=ri_pate_fermente,
				amount='16 ounces'
			)
			self.assertIn(il_pate_fermente.ingredient, french_bread.ingredients.all())
