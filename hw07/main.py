import os
#Задание 1
def my_cook_book():
    cook_book = {}
    with open('hw07/recipes.txt', encoding='utf-8') as file:
        for line in file.read().split('\n\n'):
            key, *value = line.split('\n')
            cook_book[key] = []
            count_ing = int(value[0])
            for i in range(count_ing):
                ing = value[i+1].split(' | ')
                ing_object = {}
                ing_object['ingredient_name'] = ing[0]
                ing_object['quantity'] = ing[1]
                ing_object['measure'] = ing[2]
                cook_book[key].append(ing_object)
    print(cook_book)
    return cook_book
my_cook_book()
#Задание 2
def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for i in dishes:
        recipe = cook_book[i]
        for prop in recipe:
            prop_quantity = {}
            prop_quantity['quantity'] = int(prop['quantity'])*person_count
            prop_quantity['measure'] = prop['measure']
            if prop['ingredient_name'] in ingredients:
                prop_quantity['quantity'] = int(prop['quantity'])*person_count+int(prop_quantity['quantity'])
            ingredients[prop['ingredient_name']] = prop_quantity
    print(ingredients)
    return
cook_book = my_cook_book()
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

#Задание 3
def final_file():
    with open('hw07/1.txt', encoding='utf-8') as file:
        one = file.read().split('\n')
        numb_str_one = len(one)
        path_one = os.path.join(os.getcwd(), 'hw07/1.txt')
        file_one = os.path.basename(path_one)
    with open('hw07/2.txt', encoding='utf-8') as file:
        two = file.read().split('\n')
        numb_str_two = len(two)
        path_two = os.path.join(os.getcwd(), '2.txt')
        file_two = os.path.basename(path_two)
    with open ('hw07/3.txt', encoding='utf-8') as file:
        three = file.read().split('\n')
        numb_str_three = len(three)
        path_three = os.path.join(os.getcwd(), 'hw07/3.txt')
        file_three = os.path.basename(path_three)
    string = [numb_str_one, numb_str_two, numb_str_three]
    string.sort()
    finale_f = open('hw07/result.txt', '+w', encoding='utf-8')
    for i in string:
        if i == numb_str_one:
            finale_f.write(file_one)
            finale_f.write('\n')
            finale_f.write(str(numb_str_one))
            finale_f.write('\n')
            for line in one:
                finale_f.write(line)
                finale_f.write('\n')
        elif i == numb_str_two:
            finale_f.write(file_two)
            finale_f.write('\n')
            finale_f.write(str(numb_str_two))
            finale_f.write('\n')
            for line in two:
                finale_f.write(line)
                finale_f.write('\n')
        elif i == numb_str_three:
            finale_f.write(file_three)
            finale_f.write('\n')
            finale_f.write(str(numb_str_three))
            finale_f.write('\n')
            for line in three:
                finale_f.write(line)
                finale_f.write('\n')
    finale_f.close()
    return
final_file()