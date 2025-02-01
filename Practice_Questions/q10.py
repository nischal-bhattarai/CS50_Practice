def main():
    a=float(input("Enter your First Number"))
    b=float(input("Enter your Second Number"))
    c=float(input("Enter your Third Number"))
    
    is_greater(a,b,c)

def is_greater(x,y,z):
    if x>y and x>z:
        print(f"{x} is greatest of all")
    elif y>x and y>z:
        print(f"{y} is gratest of all")
    elif z>x and z>y:
        print(f"{z} is gratest of all")
    else:
        print("All number are equal")
        
    return(x,y,z)

main()
