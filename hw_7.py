def add_ingidient(dish_recipes: dict,ingridient: str):
    item = ingridient.split("|")
    name = item[0]
    quantity = item[1]
    measure = item[2]
    new_ingredient = {
            'name': name,
            'quantity': float(quantity),
            'measure': measure
        }
    dish_recipes.append(new_ingredient)

cook_book={}

with open('recipes.txt',encoding = 'utf-8') as file:
    recipes = file.read().split('\n\n')
    for recipe in recipes:
        recipe_line = recipe.split('\n')
        dish_name = recipe_line[0]
        component = {dish_name :[]}
        dish_recepie = component[dish_name]
        for ingridient in recipe_line[2:]:
            add_ingidient(dish_recepie, ingridient)
        cook_book.update(component)



print(cook_book)