import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == 'encode':
        shifted_alphabet = alphabet[slice(shift_amount, len(alphabet))] + alphabet[slice(0, shift_amount)]
    elif cipher_direction == 'decode':
        shifted_alphabet = alphabet[slice(-shift_amount, len(alphabet))] + alphabet[slice(0, -shift_amount)]
    else:
        return print("Invalid Operation.")
    
    end_text = []
    for letter in start_text:
        try:
            end_text += shifted_alphabet[alphabet.index(letter)]
        except:
            end_text += letter
    
    print(f"The {cipher_direction}d text is: {''.join(end_text)}.")

print(art.logo)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != 'yes':
        break