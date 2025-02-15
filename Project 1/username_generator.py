import random

adjectives = ["Happy", "Cool", "Brave", "Clever", "Swift", "Mighty"]
nouns = ["Tiger", "Dragon", "Falcon", "Wolf", "Panther", "Shark"]

print("Welcome to the Random Username Generator!")

num = int(input("How many usernames do you want to generate? "))

use_numbers = input("Do you want numbers in the username? (yes/no) ")
use_specials = input("Do you want special characters in the username? (yes/no) ")

length = int(input("Enter the maximum length of the username: "))

usernames = []

for i in range(num):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun  

    if use_numbers.lower() == "yes":
        username += str(random.randint(10, 99))  
    
    if use_specials.lower() == "yes":
        username += random.choice("!@#$%^&*")  

    
    username = username[:length]

    usernames.append(username)


print("\nHere are your usernames:")
for name in usernames:
    print(name)


save = input("Do you want to save these usernames to a file? (yes/no) ")

if save.lower() == "yes":
    file = open("usernames.txt", "a")  
    for name in usernames:
        file.write(name + "\n")  
    file.close()
    print("Usernames saved to 'usernames.txt'!")

print("Thanks for using the Random Username Generator!")
