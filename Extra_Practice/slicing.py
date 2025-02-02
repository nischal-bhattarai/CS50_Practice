def main():
    user_Input=input("Enter your Thought: ").upper()
    is_reversed(user_Input)
    
def is_reversed(user_Input):
    for chars in user_Input[::-1]:
        print(chars,end=" ")
    return chars

main()