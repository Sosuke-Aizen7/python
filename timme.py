import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(t)
if (hour>=4 and hour<=10):
  print("good morning")
elif (hour>=11 and hour<=14):
  print("good evening")
elif(hour>=15 and hour<=18): 
  print("Good afternoon")   
else:
  print("Good night")