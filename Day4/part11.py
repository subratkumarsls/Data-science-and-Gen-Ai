for seconds in range(20, -1, -1):
    if seconds == 5:
        print("5 seconds left - Final Safety Check!")
    elif seconds == 0:
        print("0 seconds left - Rocket Launched! 🚀")
    else:
        print(f"{seconds} seconds left")
