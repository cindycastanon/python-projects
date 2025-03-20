import json


filename='part1pccexercises/10p11.txt'

try:
    with open(filename) as f:
      value=json.load(f)
except FileNotFoundError:
   
   number=int(input('Enter your favorite number: '))
   with open(filename,'w') as f:
      json.dump(number,f)

else:
  with open(filename) as f:
    value=json.load(f)
    print(f'Your favorite number is {value}!')