import time
count= int(input("Enter countdown start: "))
while(count >= 0):
    if(count == 0):
        print("Spandan married Eashita")
    else:
        print(count)
    time.sleep(1)
    count -= 1