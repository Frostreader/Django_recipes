from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 300,
        'сыр, г': 50,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def recipe_view(request, recipe):
    servings = int(request.GET.get('servings', 1))

    if recipe in DATA:
        recipe_data = DATA[recipe]
        scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe_data.items()}
        context = {'recipe': scaled_recipe}
        return render(request, 'calculator/index.html', context)

    else:
        recipes_list = {
            'recipe': DATA
        }
        return render(request, 'calculator/recipes_list.html', recipes_list)



