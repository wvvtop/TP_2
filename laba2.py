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
    if len(list_of_dict_of_products) == 0:
        print("Список пуст")
    elif "index" in list_of_dict_of_products[0]:
        for product in list_of_dict_of_products:
            print(f"{product["index"]}. {product["name"]} {product["category"]} (Ккал: {product["calories"]} Белки: {product["proteins"]} "
                    f"Жиры: {product["fats"]} Углеводы: {product["carbohydrates"]})")
    elif "index" not in list_of_dict_of_products[0]:
        for product in list_of_dict_of_products:
            print(f"{product["name"]} {product["category"]} (Ккал: {product["calories"]} Белки: {product["proteins"]} "
                    f"Жиры: {product["fats"]} Углеводы: {product["carbohydrates"]})")


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
                    save_json(temp_list_of_products)
                    return
            # if s == "да":
            #     save_json(temp_list_of_products)
            #     return
            # elif s == "нет":
            #     return
            # else:
            #     print("Ошибка, введите заново!")


        this_products = list(products)
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
                        this_products = [p for p in products if p["category"] == category.capitalize()]
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
                print("сортировать по (0. отмена): 1. калорийность, 2. белки, 3. жиры или 4. углеводы ")
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

            print_all_products(this_products)

        for i in range(len(this_products)):
            this_products[i]["index"] = i + 1
        print_all_products(this_products)
        product_index = input_num_more_0()
        if any(product["index"] == product_index for product in this_products):
            product = next((product for product in this_products if product["index"] == product_index), None)
            print("Введите в граммах продукт или для отменты введите '0':")
            product_weight = input_num_more_0()
            if product_weight == 0:
                continue
            elif product_weight > 0:
                product["weight"] = product_weight
                product["calories"] = round(product_weight / 100 * product["calories"], 2)
                product["proteins"] = round(product_weight / 100 * product["proteins"], 2)
                product["fats"] = round(product_weight / 100 * product["fats"], 2)
                product["carbohydrates"] = round(product_weight / 100 * product["carbohydrates"], 2)
                del product["index"]
                print_all_products([product])
                while True:
                    s = input("Добавить во временный список (да/нет)\n").lower().strip()
                    if s == "да":
                        temp_list_of_products.append(product)
                        break
                    elif s == "нет":
                        break
                    else:
                        print("Ошибка, введите заново!")
        else:
            print("Ошибка!")


while True:
    print("Введите:\n"
          "1. Суммарные характеристики набора продуктов\n"
          "2. Выбор по заданным характеристикам\n"
          "3. Сортировка по одному из параметров\n"
          "4. Вывод информации о приемах пищи")

    s = input()
    if s == "1":
        calculate()
