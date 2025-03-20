#: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

def show_messages(texts):
  for x in texts:
    print(f'{x}')
list1=['hi','yes','how are you','fun']
show_messages(list1)