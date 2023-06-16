class StoredIngredient:
    available_milk = 250
    available_coffee_beans = 250
    available_water = 750
    milk = 50
    water = 150

    @staticmethod
    def check_ingredient_availability(milk, coffee_strength):
        if milk:
            if StoredIngredient.available_milk < StoredIngredient.milk:
                return "Insufficient milk"
        if StoredIngredient.available_coffee_beans < coffee_strength:
            return "Insufficient, coffee beans"
        if StoredIngredient.available_water < StoredIngredient.water:
            return "Insufficient water"
        return

    @staticmethod
    def calculate_ingredient(milk, coffee_strength):
        if milk:
            StoredIngredient.available_milk -= StoredIngredient.milk
            StoredIngredient.available_coffee_beans -= coffee_strength
            StoredIngredient.available_water -= StoredIngredient.water
        else:
            StoredIngredient.available_coffee_beans -= coffee_strength
            StoredIngredient.available_water = StoredIngredient.available_water - (
                        StoredIngredient.water + StoredIngredient.milk)

    def make_coffee(self, milk, coffee_strength, frothed):
        message = self.check_ingredient_availability(milk, coffee_strength)
        if message:
            return message
        self.calculate_ingredient(milk, coffee_strength)
        StoredIngredient.available_coffee_beans -= coffee_strength
        if milk:
            if frothed:
                return f"your coffee has frothed milk and coffee strength is {int(coffee_strength/10)}"
            else:
                return f"your coffee has milk and coffee strength is {int(coffee_strength/10)}"
        else:
            return f"your coffee is without milk and coffee strength is {int(coffee_strength/10)}"


class Ingredient(StoredIngredient):
    def __init__(self):
        self.milk = True
        self.coffee_strength = 10
        self.frothed = False

    def collect_ingredient(self):
        self.input_milk()
        self.input_coffee_strength()
        if self.milk is True:
            self.input_foam()
        return self.make_coffee(self.milk, self.coffee_strength, self.frothed)

    def input_milk(self):
        milk = input("Do you prefer milk? yes/no: ")
        if milk.lower() == 'yes':
            self.milk = True
        elif milk.lower() == 'no':
            self.milk = False
        else:
            print("Please enter a valid preference (yes/no).")
            self.input_milk()

    def input_coffee_strength(self):
        coffee_strength = input("Enter coffee strength 1/2/3: ")
        if coffee_strength in ["1", "2", "3"]:
            self.coffee_strength = int(coffee_strength) * 10
        else:
            print("Please enter a valid preference (1/2/3).")
            self.input_coffee_strength()

    def input_foam(self):
        frothed = input("Milk should be frothed? (yes/no)")
        if frothed.lower() == 'yes' or frothed.lower() == 'no':
            self.frothed = True if frothed.lower() == 'yes' else False
        else:
            print("Please enter a valid preference (yes/no).")
            self.input_foam()


class Coffee:
    def make_coffee(self):
        while True:
            print(Ingredient().collect_ingredient())
            print()


obj = Coffee()
obj.make_coffee()
