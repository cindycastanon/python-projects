sandwich_orders=['ham','chicken','pb-jelly','cheese']
finished_sandwiches=[]
while sandwich_orders:
  get_order=sandwich_orders.pop()
  finished_sandwiches.append(get_order)

print(f'\nThe following sandwiches have been made: ')
for x in finished_sandwiches:
  print(f'{x}')
