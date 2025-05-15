# Project 1 caesar cipher
# By Ashley K.

print("Hello user! :)")
alphabet = "abcdefghijklmnopqrstuvwxyz"

question = ""
while question != "q":
    question = input("Do you want to encrypt (e), decrypt (d), or quit (q)?: ").lower()

    if question == "e":
        # Get encryption parameters:
        input_string = input("What would you like to encrypt? ").lower()
        shift = int(input("How many rotations would you like to make? (from 1 to 25): "))
        
        # Encode:
        new_encryption = ""
        for character in input_string:
            if character in alphabet:
                position = alphabet.find(character)
                new_position = (position + shift) % 26
                new_character = alphabet[new_position]
                new_encryption += new_character
            else:
                new_encryption += character
        
        # Print the encoded string:
        print(new_encryption)

    elif question == "d":
        string_to_decode = input("What would you like to decrypt?: ").lower()
        text_to_find = input("What would you like to find in the decrypted string?: ").lower()
        
        # Attempt to decode:
        shift = 0
        done = False
        while done == False:
            rotated_string = ""
            # Do one rotation:
            for character in string_to_decode:
                if character in alphabet:
                    position = alphabet.find(character)
                    new_position = (position - shift) % 26
                    new_character = alphabet[new_position]
                    rotated_string += new_character
                else:
                    rotated_string += character
            
            # If found, print the decoded string:
            if text_to_find in rotated_string or text_to_find == rotated_string:
                print(f"Found the decoded string. It requires {shift} rotations.")
                print(f"Decoded string: {rotated_string}")
                done = True
            # Else, increment the shifter:
            else:
                if shift <= 25:
                    shift += 1
                else:
                    print(f"Could not find a rotation to decrypt '{string_to_decode}'")
                    done = True

print("Thank you, have a nice day! :)")
