import random

# Recipes with their main ingredients
recipes = {
    "炒菜": {
        "宫保鸡丁": ["鸡肉", "黄瓜", "胡萝卜"],
        "炒合菜": ["鸡蛋", "豆芽", "粉条"],
        "炒猪肝": ["猪肝", "青红椒"],
        "酸辣土豆丝": ["土豆"],
        "酸辣白菜": ["白菜"],
        "番茄炒鸡蛋": ["番茄", "鸡蛋"]
    },
    "炖菜": {
        "白菜炖豆腐with鱼蛋": ["豆腐", "白菜", "鱼蛋"]
    },
    "汤": {
        "牛肉汤": ["牛肉", "白萝卜"],
        "疙瘩汤": ["白菜", "番茄"]
    }
}

# Special cold dish sauces and their compatible main ingredients
cold_dish_sauces = {
    "怪味汁": ["手撕鸡胸肉", "土豆", "胡萝卜", "黄瓜", "莴苣"],
    "凉拌菜通用汁": ["手撕鸡胸肉", "土豆", "胡萝卜", "黄瓜", "莴苣"]
}

def recommend_two_dishes(recipes, cold_dish_sauces):
    # Combine non-cold dish recipes with potential cold dish combinations
    all_dishes = {}
    for category, dishes in recipes.items():
        all_dishes.update(dishes)

    # Add cold dish sauces as potential dishes
    for sauce, ingredients in cold_dish_sauces.items():
        for ingredient in ingredients:
            all_dishes[f"{sauce} + {ingredient}"] = [ingredient]
    
    # Select the first dish
    first_dish_name = random.choice(list(all_dishes.keys()))
    first_dish_ingredients = all_dishes[first_dish_name]

    # Remove dishes with overlapping ingredients to ensure no conflict
    for dish in list(all_dishes):
        if set(all_dishes[dish]) & set(first_dish_ingredients):
            all_dishes.pop(dish)

    # Select the second dish
    second_dish_name = random.choice(list(all_dishes.keys()))

    return first_dish_name, second_dish_name

# Generate and display recommendations
first_dish, second_dish = recommend_two_dishes(recipes, cold_dish_sauces)
print(f"Today's recommended dishes are: {first_dish} and {second_dish}.")
