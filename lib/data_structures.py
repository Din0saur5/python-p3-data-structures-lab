spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
  return([food.get('name') for food in spicy_foods])
        

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get('heat_level')>5 ]

def print_spicy_foods(spicy_foods):
    return[print(f"{food.get('name')} ({food['cuisine']}) | Heat Level: {'🌶'*food['heat_level']}") for food in spicy_foods]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    return [food for food in spicy_foods if food.get('cuisine') == cuisine ].pop(0)

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    avgT = 0
    for food in spicy_foods:
        avgT += food['heat_level']
    return avgT/ len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
   spicy_foods.append(spicy_food)
   return spicy_foods
