
# КОПИРОВАНИЕ СПИСКОВ

my_cars = ['BMW, Mercedes']

# copied_cars = my_cars         # копирование списка (с добавление новых данных в оба списка)

# copied_cars = my_cars[:]      # КОПИРОВАНИЕ В НОВЫЙ СПИСОК №1 (используя slice)

# copied_cars = my_cars.copy()  # КОПИРОВАНИЕ ЧЕРЕЗ МЕТОД СПИСКОВ №2 (.copy)

# copied_cars = list(my_cars)   # КОПИРОВАНИЕ ЧЕРЕЗ СОЗДАНИЕ НОВОГО СПИСКА №3 (функция list)


copied_cars.append('Audi')

print(copied_cars)

print(my_cars)

print(id(my_cars) == id(copied_cars))
