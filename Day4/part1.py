distance = 0
while distance < 100:
    if(not distance+4>=100):
        print(f"jhon at {distance+4}m")
    else:
        print("Jhon reached goal")
        break
    if(not distance+8>=100):
        print(f"jhon at {distance+8}m")
    else:
        print("Jhon reached goal")
        break
    print(f"jhon at {distance+7}m")
    distance+=7
    