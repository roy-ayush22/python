def main():
    def countVowel():
        word = input("word: ")
        vowels = ["a", "e", "i", "o", "u"]
        count = 0

        for char in word:
            if char in vowels:
                count += 1
        print(f"vowels: {count}")
    countVowel()

main()        