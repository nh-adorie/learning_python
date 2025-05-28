alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar(original_text,shift_amount,choice):
    new_text = ""
                
    # Encrypt
    if choice.upper() == "E":
        for char in original_text:
            if char == " ":
                new_text += char
                pass
            else:
                indx = alphabet.index(char)
                if indx + shift_amount < len(alphabet):
                    new_text += alphabet[indx+shift_amount]
                else:
                    new_text += alphabet[indx+shift_amount - len(alphabet)]         

    # Decrypt    
    if choice.upper() == "D":
        for char in original_text:
            if char == " ":
                new_text += char
                pass
            else:
                indx = alphabet.index(char)         
                if indx - shift_amount > 0:
                    new_text += alphabet[indx-shift_amount]
                else:
                    new_text += alphabet[indx-shift_amount + len(alphabet)]

    return new_text

print(logo)

print("Welcome to the caesar cipher!")


while True: 
    while True:
        choice = input("Do you want to encrypt or decrypt? Type E to encrypt // D to decrypt: ").upper()
        if choice in ["E", "D"]:
            break
        else:
            print("Invalid ")

    while True:
        original_text = input("Please input your messages (a-z): ").lower()
        if all(char.isalpha() or char == " " for char in original_text):
            break
        else:
            print("Invalid ")

    while True:
        shift_amount = int(input("Please input shift number (1-25): "))
        if 1<= shift_amount <= 25:
            break      
        else:
            print("Invalid ")

    while True: 
        print(f"New text is: {caesar(original_text,shift_amount,choice)}")  
        
        continue_choice = input("\nDo you want to continue? Type E to encrypt, D to decrypt, or any other key to exit: ").upper()
        if continue_choice not in ["E", "D"]:
            print("Goodbye!")
        break
    break



    
        


