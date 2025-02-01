def main():
   try: 
    User_age=int(input("Enter Your Age"))
    is_eligible(User_age)
   except ValueError:
       print("Please Enter Valid Age")
          
def is_eligible(age):
    if age >= 18:
        print("You are Eligible to Vote")
    elif age < 18 and age>=0:
        print("You are not Eligible to Vote")
    else:
        print("Please Enter Valid Age")
         
    return age

main()
