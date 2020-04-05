cook_book = {}
list_data = []
# Task 1
def open_file(cook_book): 
  with open('cook_book_file.txt', encoding='utf8') as file_cook:
    for line in file_cook:
        dish_name = line.strip()
        quantity_ing = int(file_cook.readline().strip())
        if not dish_name:
            break
        list_data = []
        for index_igredient in range(int(quantity_ing)):
          index_igredient = file_cook.readline().strip().split("|")
          list_data.append({'ingredient_name': index_igredient[0].strip(), 'quantity': int(index_igredient[1].strip()), 'measure': index_igredient[2].strip()})
          cook_book[dish_name] = list_data

        file_cook.readline()
  print('cook_book = ')         
  for dishes, consist_list in cook_book.items():
    print(f'{dishes} : \n {consist_list}')

# Task 2
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
      for ingridient in cook_book[dish]:
        new_shop_list_item = dict(ingridient)
        key = new_shop_list_item['ingredient_name']
        list_data = []
        availability_key = shop_list.get(key)
        if availability_key  == None:
          list_data.append({'measure': new_shop_list_item['measure'], 'quantity':int(new_shop_list_item['quantity'])* person_count})
          shop_list[key] = list_data
        else:
           shop_list[key][0]["quantity"] += int(new_shop_list_item['quantity'])* person_count

    print(shop_list)
          
def in_dictionary(key, dict):
    if key in dict:
        return True
    return False
  
def cooking(cook_book):
  menu = input('Введите название блюд через запятую: ')
  menu_structure = menu.strip().split(',')
  quantity_error = True
  for i in range(len(menu_structure)):
    if in_dictionary(menu_structure[i], cook_book) == False:
       print(f'{menu_structure[i]} - такого блюда в меню нет ')
       quantity_error = False
  if quantity_error == True:
    quantity_people = int(input('Введите количество персон: '))
    if quantity_people == 1:
      print(f'Ингредиенты на {quantity_people} персону')
    elif 1 < quantity_people < 5:
      print(f'Ингредиенты на {quantity_people} персоны')
    else:
      print(f'Ингредиенты на {quantity_people} персон')
    get_shop_list_by_dishes(menu_structure, int(quantity_people))


def main():
  print('Введите команду: ')
  while True:
    user_input = input()
    if user_input == 'o':
      open_file(cook_book)
    elif user_input == 'm':
      cooking(cook_book)
    elif user_input == 'q':
      print('До свидания!')
      break

main()  