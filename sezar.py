def caesar_cipher(text, shift):
    """
    Function to encrypt a given text using Caesar cipher with a specified shift.
    Args:
    text (str): The text to be encrypted.
    shift (int): The shift amount for the Caesar cipher.
    
    Returns:
    str: The encrypted text.
    """
    encrypted_text = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the base character code based on uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around if necessary
            shifted = (ord(char) - base + shift) % 26 + base
            encrypted_text.append(chr(shifted))
        else:
            # Non-alphabet characters remain unchanged
            encrypted_text.append(char)
    return ''.join(encrypted_text)

# Main function to interact with the user
def main():
    # User input for the text
    text = input("Please enter the text: ")

    # Encrypting the text for all possible shifts from 1 to 25 and printing each result
    for shift in range(1, 26):
        result = caesar_cipher(text, shift)
        print(f"Shift {shift}: {result}")

# Call the main function to run the program
if __name__ == "__main__":
    main()
