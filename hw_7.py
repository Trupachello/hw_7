import os
from pathlib import Path

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

def merge_shop_lists(destination, source):
    for key in source.keys():
        if key in destination:
            destination[key]['quantity'] += source[key]['quantity']
        else:
            destination[key] = source[key]

def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}
    for dish in dishes:
        shop_list = {}
        for components in cook_book[dish]:
            component_name = components['name']
            component_info = {'quantity':components['quantity'] * person_count, 'measure':components['measure']}
            shop_list[component_name] = component_info
        merge_shop_lists(result, shop_list)
    return result

def get_file_content(file_path):
    file_name = os.path.basename(file_path)
    result = ""

    with open(file_path,'r', encoding = 'utf-8') as file:
        content = file.read()
        lines_count = content.count('\n') + 1
        result = f'{file_name}\n{lines_count}\n{content}\n'
    return result

def files_merge(src_directory, result_file):
    files = sorted(Path(src_directory).glob('*[0-9].txt'))
    file_content = []
    print(files)
    for file in files:
        file_content.append(get_file_content(file))
    
    file_content.sort(key=lambda x: x.count('\n'))

    with open(result_file,'w', encoding = 'utf-8') as file:
        file.write(''.join(file_content))

files_merge('.', 'result.txt')    


        



print(get_shop_list_by_dishes(['Омлет'], 3))