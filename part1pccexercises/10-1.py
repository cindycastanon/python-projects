#same output 3 times

#absolute path:
#filename='/Users/cindycastanon/python-projects/part1pccexercises/10p1learning_python.txt'
filename = '10p1learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()    #stores in a list

for line in lines:
    print(line.rstrip())