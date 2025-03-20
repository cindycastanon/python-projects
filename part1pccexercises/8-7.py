def make_album(name, title, number=None):
  album={'first name':name,'album title':title}
  if number:
    album['number of songs']=number
  return album

result=make_album('Bad Bunny',"x100pre")
print(result)

result=make_album('Taylor Swift',"1989")
print(result)

result=make_album('Rauw Alejandro',"Saturno",'5')
print(result)
