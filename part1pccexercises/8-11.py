#Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.


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
send_messages(list1[:], new_list)

print("\nFinal lists:")
print(list1)
print(new_list)