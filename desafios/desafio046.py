from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(2)
    if(c == 1):
        print("BOOM!")
