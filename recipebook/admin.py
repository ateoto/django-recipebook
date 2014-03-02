from django.contrib import admin
from django.contrib.contenttypes.models import ContentType

from recipebook.models import Ingredient, Recipe, RecipeIngredient, IngredientLine

class IngredientLineInline(admin.TabularInline):
    model = IngredientLine
    
    def get_formset(self, request, obj=None, **kwargs):
        self.parent_obj = obj
        return super(IngredientLineInline, self).get_formset(request, obj, **kwargs)


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        parent_ct = ContentType.objects.get_for_model(self.parent_obj.__class__)
        recipe_ct = ContentType.objects.get_for_model(Recipe)
        if parent_ct == recipe_ct:
            if db_field.name == 'ingredient':
                kwargs['queryset'] = RecipeIngredient.objects.all().exclude(content_type=recipe_ct, object_id=self.parent_obj.id)
        return super(IngredientLineInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientLineInline,)

admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
