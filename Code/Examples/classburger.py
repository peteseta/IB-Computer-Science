class Burger:
    def __init__(self, toppings, sauce, meat_type) -> None:
        self.toppings = toppings
        self.sauce = sauce
        self.meat_type = meat_type

    def cook_burger(self, temp):
        print(f"Cooking {self.meat_type} burger to {temp}.")


top = ["strawberries", "chocolate", "sprinkles", "ice cream", "sardines", "broccoli"]

# list of burgers
burger_list = [Burger([topping], "ketchup", "beef") for topping in top]

# dict of burgers
burger_dict = {}
for topping in top:
    burger_dict[topping] = Burger(topping, "ketchup", "beef")

# print(burger_dict)

# print(burger_dict["ice cream"])
burger_dict["ice cream"].cook_burger("well done")
