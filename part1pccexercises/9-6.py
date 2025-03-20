class Restaurant:
  def __init__(self,restaurant_name, cuisine_type):
    self.restaurant_name=restaurant_name.title()
    self.cuisine_type=cuisine_type
    self.number_served=0

  def describe_restaurant(self):
    print(f'The restaurant name is {self.restaurant_name} and the cuisine type is {self.cuisine_type}')

  def open_restaurant(self):
    print(f'The restaurant {self.restaurant_name} is open!')

  def set_number_served(self, number_served):
    self.number_served=number_served


  def increment_number_served(self, new_number):
    self.number_served+=new_number



class IceCreamStand(Restaurant):
  def _init__(self, restaurant_name, cuisine_type):
    super().__init__(restaurant_name,cuisine_type)
    

  def icecream(self):
    self.flavors=flavors
    for flavor in self.flavors:
      print(f"- {flavor.title()}")


iceCreamStand=IceCreamStand('Sarita','icecream')
flavors=['chocolate','vanilla','strawberry']

iceCreamStand.describe_restaurant()
iceCreamStand.icecream()