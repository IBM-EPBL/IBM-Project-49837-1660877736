import random,time,winsound

while True:
    temp=random.randint(1,100)
    if temp>60:
        print("alert temparature is high!")
        winsound.PlaySound("beep-07a.wav",winsound.SND_FILENAME)
    else:
        print("temparature is normal")
    time.sleep(1)
