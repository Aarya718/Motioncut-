import os

def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    return ' '.join(text.split()[::-1])

def save_to_file(reversed_text):
    with open("reversed_text.txt", "w") as file:
        file.write(reversed_text)
    print("Reversed text saved to 'reversed_text.txt'.")

def main():
    while True:
        print("\nText Reverser Menu:")
        print("1. Reverse Character Order")
        print("2. Reverse Word Order")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '3':
            print("Exiting program. Goodbye!")
            break
        
        text = input("Enter a sentence: ").strip()
        
        if not text:
            print("Error: Empty input. Please enter some text.")
            continue
        
        if choice == '1':
            result = reverse_characters(text)
        elif choice == '2':
            result = reverse_words(text)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        
        print("Reversed Text:", result)
        
        save_option = input("Would you like to save the reversed text to a file? (y/n): ")
        if save_option.lower() == 'y':
            save_to_file(result)

if __name__ == "__main__":
    main()
