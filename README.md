# XOR Shellcode Encryption Tool

**A Python script to encrypt shellcode or binary files using XOR encryption with a randomly generated key. The encrypted shellcode is saved to a file, and the encryption key is displayed.**

## 🔑 Key Features:
- **XOR Encryption**: Encrypts the input binary file (e.g., shellcode) using XOR encryption with a random key.
- **Random Key Generation**: The script generates a random key for each encryption process, making the output unique every time.
- **Key Display**: After encryption, the key is printed in a formatted hex string for easy reference.

## 📝 Usage:
```bash
python3 xor_encrypt.py <input_file> <output_file>
```
## Example
```bash
python3 xor_encrypt.py shellcode.bin encrypted_shellcode.bin
```
