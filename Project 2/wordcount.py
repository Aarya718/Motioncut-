def count_words(text):
   
    words = text.split()  
    return len(words)  

def main():
    
    print("Welcome to the Word Counter Program!")
    
    text = input("Enter a sentence or paragraph: ").strip()

    if not text:
        print("Error: You entered an empty string. Please provide valid input.")
        return
    
    word_count = count_words(text)
    print(f"\nWord Count: {word_count}")

if __name__ == "__main__":
    main()
