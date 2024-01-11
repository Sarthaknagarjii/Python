import time
currenttime = int(time.strftime("%H"))
print(currenttime)

if (int(currenttime<=12)):
    print("good morning")
elif(int(currenttime>=12)):
    print("good Afternoon")
else:
    print("good evening")