def main():
    year = int(input("Whats the Year? "))
    years(year)
    
def years(num):

    if num % 4 == 0:
        print("Leap Year")
    else:
        print("Not Leap Year")
    return num
    
main()    