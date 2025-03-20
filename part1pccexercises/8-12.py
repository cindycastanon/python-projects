def sandwich(*items):
  print(f'The items in the sandwich are: ')
  for x in items:
    print(f'{x}')

sandwich('tomato','lettuce','chicken')
sandwich('steak','carrot')
sandwich('mayo')