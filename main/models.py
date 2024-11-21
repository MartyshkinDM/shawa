from django.db import models

class Shawarma_points(models.Model):
    point_address = models.CharField(max_length=200, verbose_name="Адрес ресторана", blank=True, null=True)

    def __str__(self):
        return self.point_address

    class Meta:
        verbose_name = 'Точка продаж шаурмы'
        verbose_name_plural = 'Точки продаж шаурмы'

class Shawarmas(models.Model):
    shawarma_name = models.CharField(max_length=50, verbose_name="Название шаурмы", blank=True, null=True)
    shawarma_price = models.FloatField(verbose_name="Цена шаурмы", blank=True, null=True)
    shawarma_photo = models.ImageField(verbose_name='Иконка', null=True,upload_to='shawarmas/')
    shawarma_calories = models.CharField(max_length=50, verbose_name="Калории", blank=True, null=True)
    shawarma_proteins = models.CharField(max_length=50, verbose_name="Белки", blank=True, null=True)
    shawarma_fats = models.CharField(max_length=50, verbose_name="Жиры", blank=True, null=True)
    shawarma_carbohydrates = models.CharField(max_length=50, verbose_name="Углеводы", blank=True, null=True)
    def __str__(self):
        return self.shawarma_name

    class Meta:
        verbose_name = 'Шаурма'
        verbose_name_plural = 'Шаурмы'

class Workers(models.Model):
    worker_first_name = models.CharField(max_length=50, verbose_name="Имя работника", blank=True, null=True)
    worker_last_name = models.CharField(max_length=50, verbose_name="Фамилия работника", blank=True, null=True)
    worker_middle_name = models.CharField(max_length=50, verbose_name="Отчество работника", blank=True, null=True)
    worker_position = models.IntegerField(verbose_name="Должность работника", blank=True, null=True)
    worker_point_id = models.ForeignKey(Shawarma_points, on_delete=models.CASCADE, verbose_name="ID ресторана")

    def __str__(self):
        return f"{self.worker_first_name} {self.worker_last_name}"

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=50, verbose_name="Название ингредиента", blank=True, null=True)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

class ShawarmaIngredient(models.Model):
    belong_to = models.ForeignKey(Shawarmas, on_delete=models.CASCADE, related_name="shawarma_ingredients", verbose_name="Используется в шаурме")
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE, related_name="ingredient_shawarmas", verbose_name="Название ингредиент")
    weight = models.FloatField(verbose_name="Вес ингредиента (в граммах)", blank=True, null=True)

    def __str__(self):
        return f"{self.ingredient.ingredient_name} в {self.belong_to.shawarma_name} - {self.weight} г"

    class Meta:
        verbose_name = 'Ингредиент для шаурмы'
        verbose_name_plural = 'Ингредиенты для шаурмы'

class Drinks(models.Model):
    drink_name = models.CharField(max_length=50, verbose_name="Название напитка", blank=True, null=True)
    drink_price = models.FloatField(verbose_name="Цена напитка", blank=True, null=True)
    drink_description = models.CharField(max_length=250, verbose_name="Описание напитка", blank=True, null=True)
    drink_photo = models.ImageField(verbose_name='Иконка', null=True, upload_to='drinks/')
    drink_calories = models.CharField(max_length=50, verbose_name="Калории", blank=True, null=True)
    drink_proteins = models.CharField(max_length=50, verbose_name="Белки", blank=True, null=True)
    drink_fats = models.CharField(max_length=50, verbose_name="Жиры", blank=True, null=True)
    drink_carbohydrates = models.CharField(max_length=50, verbose_name="Углеводы", blank=True, null=True)
    def __str__(self):
        return self.drink_name

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'


class Snacks(models.Model):
    snack_name = models.CharField(max_length=50, verbose_name="Название снека", blank=True, null=True)
    snack_price = models.FloatField(verbose_name="Цена снека", blank=True, null=True)
    snack_description = models.CharField(max_length=250, verbose_name="Описание снека", blank=True, null=True)
    snack_photo = models.ImageField(verbose_name='Иконка', null=True, upload_to='snacks/')
    snack_calories = models.CharField(max_length=50, verbose_name="Калории", blank=True, null=True)
    snack_proteins = models.CharField(max_length=50, verbose_name="Белки", blank=True, null=True)
    snack_fats = models.CharField(max_length=50, verbose_name="Жиры", blank=True, null=True)
    snack_carbohydrates = models.CharField(max_length=50, verbose_name="Углеводы", blank=True, null=True)
    def __str__(self):
        return self.snack_name

    class Meta:
        verbose_name = 'Снек'
        verbose_name_plural = 'Снеки'

class Combos(models.Model):
    combo_name = models.CharField(max_length=50, verbose_name="Название комбо-набора", blank=True, null=True)
    combo_price = models.FloatField(verbose_name="Цена комбо-набора", blank=True, null=True)
    combo_main = models.ForeignKey(Shawarmas, on_delete=models.CASCADE, verbose_name="Блюдо в наборе")
    combo_drink = models.ForeignKey(Drinks, on_delete=models.CASCADE, verbose_name="Напиток в наборе")
    combo_snacks = models.ForeignKey(Snacks, on_delete=models.CASCADE, verbose_name="Снек в наборе")
    combo_photo = models.ImageField(verbose_name='Иконка', null=True, upload_to='combos/')

    def __str__(self):
        return self.combo_name

    class Meta:
        verbose_name = 'Комбо'
        verbose_name_plural = 'Комбо'
