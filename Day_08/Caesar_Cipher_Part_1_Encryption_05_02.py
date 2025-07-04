alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount): 
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:  # Ensure we only shift letters
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26  # Wrap around using modulo
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter  # Keep spaces and special characters unchanged
    print(f"The encoded text is {cipher_text}")

encrypt(plain_text=text, shift_amount=shift)