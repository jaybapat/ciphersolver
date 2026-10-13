def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isupper():
            plaintext += (chr((ord(char) - (key + 65)) % 26 + 65))
        elif char.islower():
            plaintext += (chr((ord(char) - (key + 97)) % 26 + 97))
        else:
            plaintext += char
    return plaintext

ciphertext = input("What is the ciphertext: ")
key = range(1,26)
for k in key:
    plaintext = caesar_decrypt(ciphertext, k)
    print(f"Key = {k};The plaintext is: {plaintext} ")