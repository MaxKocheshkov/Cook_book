cook_book = {}
list_data = []
# Task 1
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

  