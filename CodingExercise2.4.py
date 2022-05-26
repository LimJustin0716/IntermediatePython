flavors = ["chocolate", "strawberry", "cookies n' cream", "bubblegum"]
toppings = ["almods", "banana slices", "chocolate syrup", "caramel syrup", "white chocolate chips"]
ice_cream = dict(zip(flavors, toppings))
print(ice_cream)

ice_cream["chocolate"] = "blueberries"
ice_cream.update({"matcha": "pistachio", "ube": "mango slices"})
print(ice_cream)