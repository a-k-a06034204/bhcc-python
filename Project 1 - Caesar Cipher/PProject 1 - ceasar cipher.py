# By terra-ko
# Project 1 caesar cipher
print("Hello user! :)")
xyz = "abcdefghijklmnopqrstuvwxyz"
new_encryption = ""
question = input("Do you want to encrypt, decrypt, or quit?: ").lower()
if question == "e":
    question_e = input("You chose encrypt. Is that correct? (y/n): " ).lower() 
    if question_e == "y":
        encryption = input("What would you like to encrypt? ").lower()
    shift = int(input("How many rotations would you like to make? (1 to 25): "))
    for character in encryption:
         if character in xyz:
            position = xyz.find(character)
            new_position = (position + shift) % 26
            new_character = xyz[new_position]
            new_encryption += new_character
    print(new_encryption)
    question = input("Do you want to encrypt, decrypt, or quit?: ").lower()
elif question == "d":
    question_d = input("You chose decrypt. Is that correct? (y/n): ").lower()  
    if question_d == "y":
        decryption = input("What would you like to decrypt?: ").lower()
        shift = int(input("How many rotations would you like to make? (1 to 25): "))
        for character in decryption:
            position = xyz.find(character)
            new_position = (position - shift) % 26
            new_character = xyz[new_position]
            new_encryption += new_character
    print(new_encryption)
    question = input("Do you want to encrypt, decrypt, or quit?: ").lower()
elif question == "q":
    exit_question = input("Are you sure you want to quit (y/n)? ").lower()  
    if exit_question == "y":
            print("Thank you, have a nice day! :)")
            
    
   
    




