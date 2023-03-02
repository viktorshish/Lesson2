"""

Домашнее задание №1
Цикл for: Продажи товаров
* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров

"""
phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

# Cуммарное количество продаж для каждого товара
for phone in phones:
    print(f'Суммарное количество продаж для {phone["product"]}: {sum(phone["items_sold"])}')

sum_all_solds = 0
# среднее количество продаж для каждого товара
for phone in phones:
    avg_count_sold = int(sum(phone["items_sold"]) / len(phone["items_sold"]))
    print(f'Cреднее количество продаж для {phone["product"]}: {avg_count_sold}')

    # суммарное количество продаж всех товаров
    sum_all_solds += sum(phone["items_sold"])

# среднее количество продаж всех товаров
avg_all_solds = int(sum_all_solds / len(phones))

if __name__ == "__main__":
    print(f'Суммарное количество продаж всех товаров: {sum_all_solds}')
    print(f'Cреднее количество продаж всех товаров: {avg_all_solds}')
