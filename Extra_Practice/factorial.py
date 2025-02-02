def main():
    user_Input= int(input("Enter your Number: "))
    print(factorial(user_Input))
    
def factorial(user_Input):
    
    if user_Input == 1 or user_Input==0:
        return 1
    
    return user_Input * factorial(user_Input - 1)


main()

