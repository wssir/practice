#ceasor cipher


def encrypt(key, message):
    
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter)+ key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt(key,message):

    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) %len(alpha)

            result = result +alpha[letter_index]
        else:
            result = result + letter

    return result

def main():
    text = input("enter the text: ")
    shift = int(input("enter the shift key: "))
    
    encrypted = encrypt(shift,text)
    print("your text is now encrypted : ", encrypted)

    decrypted = decrypt(shift,encrypted)
    print("Original text is :",decrypted)

if __name__ == "__main__":
    main()

