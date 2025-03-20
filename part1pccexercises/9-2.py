class Restaurant:
  def __init__(self,restaurant_name, cuisine_type):
    self.restaurant_name=restaurant_name.title()
    self.cuisine_type=cuisine_type

  def describe_restaurant(self):
    print(f'The restaurant name is {self.restaurant_name} and the cuisine type is {self.cuisine_type}.')

  def open_restaurant(self):
    print(f'The restaurant {self.restaurant_name} is open!')


restaurant1=Restaurant('Chipotle','burritos')
restaurant2=Restaurant('Chilis','vegetarian')
restaurant3=Restaurant('McDonalds','burgers')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()