from django.contrib import admin

from recipebook.models import Ingredient, Recipe, IngredientLine

class IngredientLineInline(admin.TabularInline):
	model = IngredientLine

class RecipeAdmin(admin.ModelAdmin):
	inlines = (IngredientLineInline,)

admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
