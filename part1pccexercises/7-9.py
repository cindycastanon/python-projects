sandwich_orders=['pastrami','ham','pastrami','chicken','pb-jelly','cheese','pastrami']
print("We've run out of pastrami!")
while 'pastrami' in sandwich_orders:
  sandwich_orders.remove('pastrami')
print(sandwich_orders)