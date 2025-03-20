filename='/Users/cindycastanon/python-projects/part1pccexercises/10p3guest.txt'

user=input(f'Enter your name:')
with open(filename,'w') as f:
  f.write(user)