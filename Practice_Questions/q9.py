def main():
    string=input()
    string_empty(string)
    
def string_empty(s):
    if len(s) == 0:
        print("Empty")
    else:
        print("Not Empty")
    return s


main()