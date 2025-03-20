class Restaurant:
  def __init__(self,restaurant_name, cuisine_type):
    self.restaurant_name=restaurant_name.title()
    self.cuisine_type=cuisine_type

  def describe_restaurant(self):
    print(f'The restaurant name is {self.restaurant_name} and the cuisine type is {self.cuisine_type}')

  def open_restaurant(self):
    print(f'The restaurant {self.restaurant_name} is open!')

#make an instance and call two attributes individually
restaurant=Restaurant('Chipotle', 'fast food')
print(f'Restaurant:\n{restaurant.restaurant_name}\nCuisine Type:\n{restaurant.cuisine_type}')

#call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
