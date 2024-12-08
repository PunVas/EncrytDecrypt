### README for Encryption-Decryption Program

---

# Encryptor and Decryptor by PunV

This project is an encryption-decryption tool designed for basic text obfuscation. It encrypts user-provided text into a secure format and generates a decryption key for safe communication. The decryption key is necessary to restore the original text, ensuring that only authorized users can access the information.

---

## Features

1. **Text Encryption:**
   - Converts plaintext into a scrambled format based on user input and random configurations.
   - Adds padding to ensure consistency in grid-based encryption.
   - Saves the encrypted text to a file for secure storage.

2. **Decryption:**
   - Reads encrypted text from a file.
   - Uses a decryption key to restore the original text.
   - Outputs the decrypted text and saves it to a file.

3. **Key Management:**
   - Dynamically generates a unique decryption key for each encrypted text.
   - Copies the key to the clipboard for easy sharing.

---

## How It Works

1. **Encryption Process:**
   - The input text is structured into a grid with a random number of columns.
   - The text is rearranged column-wise and padded as needed.
   - The scrambled output is saved to an encrypted file.

2. **Key Generation:**
   - The key combines encoded information about the grid dimensions and random characters.
   - The key is essential for decrypting the text.

3. **Decryption Process:**
   - Reads the encrypted file.
   - Uses the key to reverse the grid-based scrambling and retrieve the original text.
   - Outputs and saves the decrypted content.

---

## Usage

### Prerequisites
- Python 3.x
- `pyperclip` library (`pip install pyperclip`)

### Steps to Run

1. **Encryption:**
   - Run the encryptor script.
   - Provide the text to be encrypted.
   - Retrieve the decryption key from the console (copied to the clipboard).
   - The encrypted text is saved in `encrypted_file.encpunv`.

2. **Decryption:**
   - Run the decryptor script.
   - Enter the decryption key.
   - The decrypted text is saved in `decrypted_file.decpunv` and displayed in the console.

---

## Files Generated
- `encrypted_file.encpunv`: Contains the encrypted text.
- `decrypted_file.decpunv`: Contains the decrypted text.

---

## Notes

- **Security Disclaimer:** The encryption method is for learning and demonstration purposes. It is not secure for critical or sensitive data.
- **Data Loss:** Ensure you keep the decryption key safe; losing it will make decryption impossible.
