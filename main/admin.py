from django.contrib import admin
from . import models

admin.site.register(models.Shawarmas)
admin.site.register(models.Snacks)
admin.site.register(models.Drinks)
admin.site.register(models.Combos)
admin.site.register(models.Shawarma_points)
admin.site.register(models.Workers)
admin.site.register(models.Ingredients)
admin.site.register(models.ShawarmaIngredient)