def main():
    number=int(input("Enter Your Number: "))
    ten_multiple(number)

def ten_multiple(num):
    if num % 10 == 0:
        print("Multiple of Ten")
    else:
        print("Not Multiple of Ten")
    return num


main()
