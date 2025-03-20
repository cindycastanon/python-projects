#Make a list, then make a copy of list. Add a new pizza to the original list. Add a different pizza to the list friend_pizzas. Prove that you have two separate lists.
pizzas=['pepperoni','ham','pineapple']
friend_pizzas=pizzas[:]
pizzas.append('italian')
friend_pizzas.append('steak')

print('My favorite pizzas are:')

my_piz=[value for value in pizzas]
print(my_piz)

# print(f"\nMy friend’s favorite pizzas are:")
# friend_piz=[value for value in friend_pizzas]
# print(friend_piz)

print(f"\nMy friend’s favorite pizzas are:")
for value in friend_pizzas:
  print(f'{value}')