import json

with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)["categories"]


def get_products(type_of_product):
    index = 0
    this_products = []
    for category in products:
        if category["name"].lower() == type_of_product.lower():  # Игнорируем регистр
            for product in category["products"]:
                index += 1
                this_product = {"index": index, "name": product["name"], "calories": product["calories"],
                                "proteins": product["proteins"], "fats": product["fats"],
                                "carbohydrates": product["carbohydrates"]}
                this_products.append(this_product)
            break
    if index == 0:
        return None
    else:
        return this_products

def print_all_products(list_of_dict_of_products):
    if len(list_of_dict_of_products) == 0:
        print("Список пуст")
    elif "index" in list_of_dict_of_products[0]:
        for product in list_of_dict_of_products:
            print(f"{product["index"]}. {product["name"]} (Ккал: {product["calories"]} Белки: {product["proteins"]} "
                f"Жиры: {product["fats"]} Углеводы: {product["carbohydrates"]})")
    elif "index" not in list_of_dict_of_products[0]:
        for product in list_of_dict_of_products:
            print(f"{product["name"]} (Ккал: {product["calories"]} Белки: {product["proteins"] }"
                f"Жиры: {product["fats"]} Углеводы: {product["carbohydrates"]})")


def print_categories():
    for category in products:
        print(category["name"])


def input_weight():
    while True:
        try:
            num = float(input("Введите в граммах продукт или для отменты введите '0':\n"))
            if num < 0:
                print("Вы ввели отрицательное значение")
                continue
            return num
        except Exception:
            print("Ошибка в числе!")


def save_json(list_to_add):
    name_of_file = "listOfDishes.json"
    with open(name_of_file, "r", encoding="utf-8") as file:
        new_product = json.load(file)
    #for i in new_product["categories"]:

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

def calculate():
    temp_list_of_products = []
    while True:
        if len(temp_list_of_products) > 0:
            print_all_products_specs(temp_list_of_products)
            print("---------------------")
        print("Нужн")
        print("Введите категорию (или введите '0' для выхода):")
        print_categories()
        category = input()
        if category == "0":
            if len(temp_list_of_products) == 0:
                return
            while True:
                s = input("Сохранить список рациона? (да/нет)\n").lower().strip()
                if s == "да":
                    save_json(temp_list_of_products)
                    return
                elif s == "нет":
                    return
                else:
                    print("Ошибка, введите заново!")

        this_products = get_products(category)
        if this_products is None:
            print("Категория не найдена. Попробуйте еще раз.")
            continue
        else:
            print_all_products(this_products)
        product_index = input("Введите номер предложенного продукта из списка (или введите '0' для выхода):\n")
        if any(str(product["index"]) == product_index for product in this_products):
            product = next((product for product in this_products if str(product["index"]) == product_index), None)
            product_weight = input_weight()
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
                #this_product[""]




        else:
            print("wwww")
        # productc_sum


while True:
    print("Введите:\n"
          "1. Суммарные характеристики набора продуктов\n"
          "2. Выбор по заданным характеристикам\n"
          "3. Сортировка по одному из параметров\n"
          "4. Вывод информации о приемах пищи")

    s = input()
    if s == "1":
        calculate()
