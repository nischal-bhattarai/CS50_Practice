def main():
    user_Input=input("Enter your Sentence")
    print((f"There are {counted(user_Input)} words in the Sentence"))
    
    
def counted(words):
    count = 0
    for word in words.split():
        count+=1
   
    return count
    
main()