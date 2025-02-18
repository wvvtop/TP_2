import json

with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)["categories"]


# print(products["categories"][0]["products"])

def print_products(type):
    found = False
    for category in products:
        if category["name"].lower() == type.lower():  # Игнорируем регистр
            found = True
            print(f"\nПродукты в категории '{type}':")
            for product in category["products"]:
                print(
                    f"  - {product['name']} (Ккал: {product['calories']}, Б: {product['proteins']}г, Ж: {product['fats']}г, У: {product['carbohydrates']}г)")
            break
    if not found:
        print("Категория не найдена. Попробуйте еще раз.")


def print_categories():
    for category in products:
        print(category["name"])


def input_int():
    while True:
        try:
            num = float(input("Введите в граммах продукт или для отменты введите '0':\n"))
            return num
        except Exception:
            print("Ошибка в числе!")


def save_json(list_to_add):
    name_of_file = "listOfDishes.json"
    with open(name_of_file, "r", encoding="utf-8") as file:
        new_product = json.load(file)
    #for i in new_product["categories"]:


def calculate():
    products_sum = []
    while True:
        print_categories()
        category = input("Введите категорию:\n")
        print_products(category)
        product = input("Введите предложенный продукт из списка:\n")
        if any(p["name"].lower() == product.lower() for c in products for p in c["products"]):
            product_weight = input_int()
            if product_weight == 0:
                continue
            elif product_weight > 0:
                this_product = next(
                    (p | {"weight": 0} for c in products for p in c["products"] if product in p["name"].lower()),
                    None
                )
                this_product["calories"] = product_weight / 100 * this_product["calories"]
                this_product["proteins"] = product_weight / 100 * this_product["proteins"]
                this_product["fats"] = product_weight / 100 * this_product["fats"]
                this_product["carbohydrates"] = product_weight / 100 * this_product["carbohydrates"]
                this_product[""]
                ###
                print()


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
