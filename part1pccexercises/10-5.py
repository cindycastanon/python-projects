

# print("Enter 'quit when done: ")
# while True:
#   reason=input('Why do you like programming? ')
#   if reason=='quit':
#     break
#   else:
#     filename='/Users/cindycastanon/python-projects/part1pccexercises/10p5reason.txt'
#     with open(filename,'a') as f:
#         f.write(f'{reason}\n')


filename='/Users/cindycastanon/python-projects/part1pccexercises/10p5reason.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break
    else:
        with open(filename, 'a') as f:
          for response in responses:
              f.write(f"{response}\n")