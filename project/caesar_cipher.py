# Encryption

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text,shift_amount):

    encrypted_list = []

    for char in original_text:

        indx = alphabet.index(char) # Trả về indx của chữ cái (char) trong bảng chữ cái (alphabet)
        if indx + shift_amount < len(alphabet):
             encrypted_list.append(alphabet[indx+shift_amount]) # Thêm vào str chữ cái tại index trong bảng chữ cái là indx + shift_amount
        else:
             encrypted_list.append(alphabet[indx+shift_amount - len(alphabet)])             

        encrypted_text = "".join(encrypted_list)

    return encrypted_text

try:
    original_text = input("Please input your messages: ")
    shift_amount = int(input("Please input shift amount: "))

    print(f"Encypted text is: {encrypt(original_text,shift_amount)}")   


except Exception as e:
       # By this way we can know about the type of error occurring
        print("The error is: ",e)





    
        


