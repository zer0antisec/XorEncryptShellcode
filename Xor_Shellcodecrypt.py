import os
import sys

def xor_encrypt(data, key):
    key_len = len(key)
    return bytes([data[i] ^ key[i % key_len] for i in range(len(data))])

def main(input_file, output_file):
    # Leer el contenido del archivo .bin
    with open(input_file, 'rb') as f:
        shellcode = f.read()

    # Generar clave aleatoria
    key = os.urandom(16)  # Cambia el tamaño de la clave según sea necesario

    # Encriptar la shellcode
    encrypted_shellcode = xor_encrypt(shellcode, key)

    # Guardar la shellcode encriptada en un archivo
    with open(output_file, 'wb') as f:
        f.write(encrypted_shellcode)

    # Imprimir la shellcode encriptada y la clave
    print(f"Shellcode encriptada guardada en '{output_file}'.")
    
    print("\nClave:")
    print(', '.join(f'0x{byte:02X}' for byte in key))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <archivo_entrada> <archivo_salida>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    main(input_file, output_file)
