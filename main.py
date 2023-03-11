# Словарь с исползованием переменных
brand = 'Ducati'
bike_price = 25000
engine_volume = 1.2

my_motorbike = {
    'brand': brand,
    'price': bike_price,
    'engine_vol': engine_volume
}
print(my_motorbike)
# Словарь (Обычный)
# my_motorbike = {
#     'brand': 'Ducati',
#     'price': '25000',
#     'engine_vol': 1.2
# }

# Метод .get если не уверен в налии ключа в словаре( если нет - вернет значение после запятой)
print(my_motorbike.get('model', 123))

# Если уверен
print(my_motorbike['brand'])
print(my_motorbike.get('brand'))

# Удаление из словаря
del my_motorbike['price']

# Длинна словаря
print(len(my_motorbike))

# Замена элемента
my_motorbike['engine_vol'] = 1.8
print(my_motorbike['engine_vol'])

# Доступ к значению элемента с помощью переменной
key_name = 'brand'
my_motorbike[key_name] = 'BMW'
print(my_motorbike['brand'])

# Добавление элементов
my_motorbike['is_new'] = True
print(my_motorbike['is_new'])
