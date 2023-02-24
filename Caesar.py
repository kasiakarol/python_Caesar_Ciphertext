from Caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
print("Welcome to Caesar! You can either encrypt or decrypt your message.")


def play_again():
    if_play_again = input("Would you like to encode or decode again? Y/N: ")
    if if_play_again.upper() == "Y":
        return True


while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        text_caesar = input("Type your message:\n").lower()
        try:
            shift_caesar = int(input("Type the shift number:\n"))
        except ValueError:
            print("Incorrect input.")
            break
        if shift_caesar > 26:
            shift_caesar = shift_caesar % 26

        caesar_new = ""
        for letter in text_caesar:
            if letter not in alphabet:
                caesar_new += letter
            else:
                position = alphabet.index(letter)
                if direction == "encode":
                    new_position = (position + shift_caesar) % 26
                    new_letter = alphabet[new_position]
                    caesar_new += new_letter
                else:
                    new_position = (position - shift_caesar) % 26
                    new_letter = alphabet[new_position]
                    caesar_new += new_letter

        if direction == 'encode':
            print(f"Your encoded message is: '{caesar_new}'")
        else:
            print(f"Your decoded message is: '{caesar_new}'")

    else:
        print("Incorrect input.")
        if play_again():
            continue
        else:
            break

    if not play_again():
        break
