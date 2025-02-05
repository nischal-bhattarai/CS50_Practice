def main():
    x = get_int()
    print(f"X is {x}")
    
def get_int():
    while True:
        try:
            x = int(input("Whats X? "))
        except ValueError:
            print("X is not an Integer")
        else:
            return x

main()
