import json

with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)


def get_products(type_of_product):
    index = 0
    this_products = []
    for product in products:
        index += 1
        if type_of_product == "all":
            this_product = {"index": index, "name": product["name"], "calories": product["calories"],
                            "proteins": product["proteins"], "fats": product["fats"],
                            "carbohydrates": product["carbohydrates"]}
        elif product["category"] == type_of_product:
            this_product = {"index": index, "name": product["name"], "calories": product["calories"],
                            "proteins": product["proteins"], "fats": product["fats"],
                            "carbohydrates": product["carbohydrates"]}
        this_products.append(this_product)
    if index == 0:
        return None
    else:
        return this_products

def print_all_products(list_of_dict_of_products):
    if not list_of_dict_of_products:  # Проверка на пустой список
        print("Список пуст")
        return

    for product in list_of_dict_of_products:
        if "index" in product:  # Проверяем, есть ли ключ "index"
            print(f"{product['index']}. {product['name']} {product['category']} "
                    f"(Ккал: {product['calories']}, Белки: {product['proteins']}, "
                    f"Жиры: {product['fats']}, Углеводы: {product['carbohydrates']})")
        else:
            print(f"{product['name']} {product['category']} "
                    f"(Ккал: {product['calories']}, Белки: {product['proteins']}, "
                    f"Жиры: {product['fats']}, Углеводы: {product['carbohydrates']})")



def print_categories():
    s = set()
    for product in products:
        s.add(product["category"])
    for i in s:
        print(i)

def get_categories():
    s = set()
    for product in products:
        s.add(product["category"])
    return s

def input_num_more_0():
    while True:
        try:
            num = float(input())
            if num < 0:
                print("Вы ввели отрицательное значение\n"
                      "Введите число или для отменты введите '0':\n")
                continue
            return num
        except Exception:
            print("Ошибка в числе!")


def save_json(temp_list_of_products):
    filename = "listOfDishes.json"
    try:
        # Читаем уже сохранённые данные, если файл существует
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                if not isinstance(data, list):  # Если в файле не список, перезаписываем
                    data = []
        except (FileNotFoundError, json.JSONDecodeError):
            data = []  # Если файла нет или он пустой, создаём новый список

        # Добавляем новый список продуктов в общий список
        data.append(temp_list_of_products)

        # Записываем обратно в файл
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Список продуктов успешно добавлен в {filename}!")

    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def print_all_products_specs(list_of_dict_of_products):
    total_product = {"calories": 0, "proteins": 0, "fats": 0, "carbohydrates": 0, "weight": 0}
    for product in list_of_dict_of_products:
        total_product["calories"] += product["calories"]
        total_product["proteins"] += product["proteins"]
        total_product["fats"] += product["fats"]
        total_product["carbohydrates"] += product["carbohydrates"]
        total_product["weight"] += product["weight"]
    print(f"Всего вышло (Ккал: {total_product["calories"]} Белки: {total_product["proteins"]}"
          f"Жиры: {total_product["fats"]} Углеводы: {total_product["carbohydrates"]} Общий вес: {total_product["weight"]})")

def yes_no():
    while True:
        s = input()
        if s == "да":
            return True
        elif s == "нет":
            return False
        else:
            print("Ошибка, введите заново!")


import copy


def calculate():
    temp_list_of_products = []
    while True:
        if len(temp_list_of_products) > 0:
            print_all_products_specs(temp_list_of_products)
            print("---------------------")
            print("Хотите ли продолжить? (да/нет)\n")
            if not yes_no():
                print("Хотите ли сохранить в файл? (да/нет)")
                if yes_no():
                    # Перед сохранением удаляем index из всех продуктов
                    for product in temp_list_of_products:
                        product.pop("index", None)
                    save_json(temp_list_of_products)
                    return

        # Создаём полную копию списка продуктов, чтобы не изменять оригинал
        this_products = copy.deepcopy(products)

        print("Нужны ли какие-то фильтры при работе? (да/нет)")
        if yes_no():
            print("Введите номера фильтров через пробел:\n"
                  "1. категория продукта,\n"
                  "2. сортировать у которых меньше Ккал чем n,\n"
                  "3. сортировать по: калорийность, белки, жиры или углеводы\n"
                  " или нажмите интер, чтобы пропустить")
            filters = input().strip().split()

            if "1" in filters:
                print("Введите категорию или введите '0.' чтобы не вводить фильтр")
                print_categories()
                while True:
                    category = input()
                    if category.lower() in [i.lower() for i in get_categories()]:
                        this_products = [p for p in this_products if p["category"] == category.capitalize()]
                        break
                    elif category == "0":
                        break
                    else:
                        print("Такой категории нет, введи заново!")

            if "2" in filters:
                print("Введите число для сортировки меньше введенного или введите '0.' чтобы не вводить фильтр")
                num = input_num_more_0()
                if num == 0:
                    break
                this_products = [i for i in this_products if i["calories"] < num]

            if "3" in filters:
                print("Сортировать по (0. отмена): 1. калорийность, 2. белки, 3. жиры или 4. углеводы ")
                while True:
                    num = input()
                    if num == "0":
                        break
                    elif num == "1":
                        this_products = sorted(this_products, key=lambda p: p["calories"], reverse=True)
                        break
                    elif num == "2":
                        this_products = sorted(this_products, key=lambda p: p["proteins"], reverse=True)
                        break
                    elif num == "3":
                        this_products = sorted(this_products, key=lambda p: p["fats"], reverse=True)
                        break
                    elif num == "4":
                        this_products = sorted(this_products, key=lambda p: p["carbohydrates"], reverse=True)
                        break

        if not this_products:
            print("Итоговый список пуст")
            continue

        # Добавляем индекс к продуктам (но только в копии, а не в оригинале!)
        for i, product in enumerate(this_products, start=1):
            product["index"] = i

        print_all_products(this_products)

        product_index = input_num_more_0()
        product = next((p for p in this_products if p["index"] == product_index), None)

        if product:
            print("Введите в граммах продукт или для отмены введите '0':")
            product_weight = input_num_more_0()
            if product_weight == 0:
                continue

            # Создаём копию продукта перед изменениями
            product_copy = copy.deepcopy(product)

            product_copy["weight"] = product_weight
            product_copy["calories"] = round(product_weight / 100 * product_copy["calories"], 2)
            product_copy["proteins"] = round(product_weight / 100 * product_copy["proteins"], 2)
            product_copy["fats"] = round(product_weight / 100 * product_copy["fats"], 2)
            product_copy["carbohydrates"] = round(product_weight / 100 * product_copy["carbohydrates"], 2)

            # Удаляем index перед добавлением в список (чтобы не сохранялся в JSON)
            product_copy.pop("index", None)

            print_all_products([product_copy])
            while True:
                s = input("Добавить во временный список (да/нет)\n").lower().strip()
                if s == "да":
                    temp_list_of_products.append(product_copy)
                    break
                elif s == "нет":
                    break
                else:
                    print("Ошибка, введите заново!")
        else:
            print("Ошибка!")


def demonstrate_diet():
    with open("listOfDishes.json", "r", encoding="utf-8") as file1:
        list_of_diet = json.load(file1)
    for i in list_of_diet:
        print_all_products(list(i))
        print_all_products_specs(list(i))
        print("----------------------")



while True:
    print("Введите:\n"
          "1. Суммарные характеристики набора продуктов\n"
          "2. Вывести прошлые рационы")

    s = input()
    if s == "1":
        calculate()
    elif s == "2":
        demonstrate_diet()

