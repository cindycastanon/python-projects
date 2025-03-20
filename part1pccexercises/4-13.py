#Use a for loop to print each food the restaurant offers. Try to modify one of the items, and make sure that Python rejects the change.The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

tuple=('pizza','burger','steak','baleada','chicken')
for value in tuple:
  print(value)

#tuple[0]='pasta'      #type error bc tuples are immutable

tuple=('spaghetti','pasta','steak','baleada','chicken')
print(f'\nRevised tuple:')
for value in tuple:
  print(value)