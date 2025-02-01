def main():
    Character=input("Your Character").lower()
    vowel_consonant(Character)

def vowel_consonant(char):
    if char in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
    return char


main()
    