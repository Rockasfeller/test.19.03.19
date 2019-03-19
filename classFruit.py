class Fruit:
    def __init__(self, name, color, country, price):
        self.name = name
        self.color = color
        self.country = country
        self.price = price
    def print_info(self):
        print (self.name + "," + self.color + "," +  self.country + ","  + str (self.price)) 
        
    def change_price(self, new_price):
        self.price = new_price
            
    def change_color(self, new_color):
        self.color = new_color





fruit_obj1 = Fruit ("Banana", "red", "Panama", 78)
fruit_obj2 = Fruit ("Orange", "orange", "Turkey", 65)
fruit_obj3 = Fruit ("Apple", "green", "Russia", 35)

fruit_obj1.print_info()
fruit_obj2.print_info()
fruit_obj3.print_info()

fruit_obj1.change_price(100)




fruit_obj3.change_color("red")

fruit_obj1.print_info()
fruit_obj2.print_info()
fruit_obj3.print_info()