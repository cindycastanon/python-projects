def make_album(name, title, number=None):
  album={'first name':name,'album title':title}
  if number:
    album['number of songs']=number
  return album


while True:
  artist=(input('Enter an artist: '))
  if artist=='quit':
    break
  
  title1=(input('Enter an album from this artist: '))
  if title1=='quit':
    break
  
  
  result=make_album(artist,title1)
  print(result)

print("\nThanks for responding!")

# result=make_album('Bad Bunny',"x100pre")
# print(result)

# result=make_album('Taylor Swift',"1989")
# print(result)

# result=make_album('Rauw Alejandro',"Saturno",'5')
# print(result)
