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

  
restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1257)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(239)
print(f"Number served: {restaurant.number_served}")