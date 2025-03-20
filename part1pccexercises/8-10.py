#Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.


def show_messages(texts):
  print(f'The message shown are: ')
  for x in texts:
    print(f'{x}')




def send_messages(list1, new_list):
  print(f'The messages sent are: ')
  while list1:
    get=list1.pop()
    new_list.append(get)
    for text in new_list:
      print(text)
  


list1=['hi','yes','how are you','fun']
new_list=[]


show_messages(list1)
send_messages(list1, new_list)

print("\nFinal lists:")
print(list1)
print(new_list)