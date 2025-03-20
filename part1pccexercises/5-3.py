#if you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of independent if statements.


#Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
alien='green'
if alien == 'green':
  print('Player earned 5 points!')


#Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
alien='green'
if alien == 'green':
  print('Player earned 5 points!')

if alien == 'blue':
  print('Player earned 5 points!')