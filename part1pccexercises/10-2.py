
filename = '/Users/cindycastanon/python-projects/part1pccexercises/10p1learning_python.txt'
with open(filename) as lp:
  lines=lp.readlines()


for line in lines:
  line=line.rstrip()
  print(line.replace('Python','C'))

