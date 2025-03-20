car="subaru"
if car == "subaru":
  print("Correct!")

pizza='pineapple'
if pizza != 'pineapple':
  print('Incorrect')

color='Blue'
color.lower()=='blue'
print(color)

age = 17
if age >= 18:
 print("You are old enough to vote!")
 print("Have you registered to vote yet?")
else:
 print("Sorry, you are too young to vote.")
 print("Please register to vote as soon as you turn 18!")

shoes=2
if shoes > 2 and shoes <10:
  print('You have around an average amount of shoes.')

elif shoes<2 or shoes>=1:
  print("You don't have enough shoes.")

#test if item is in a list
pizza=['steak','pineapple','pepperoni','ham']
type='chicken'
if type in pizza:
  print(f'{type.title()} is in our list')

#test if item is not in a list
if type not in pizza:
  print(f'{type.title()} is not in our list')