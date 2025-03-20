#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
cubes=[]
for cube in range(1,11):
  print(cube**3)
  #or cubes.append(cube**3), then print(cubes) outside loop to print a list

