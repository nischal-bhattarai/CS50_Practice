while True:
    try:
        x = int(input("Whats X? "))
    except ValueError:
        print("X is not an Integer")
    else:
        break
print(f"X is {x}")