def caesar_decrypt(ciphertext, key):
    results = ""
    for char in ciphertext:
        if char.isupper():
            results += (chr((ord(char) - (key + 65)) % 26 + 65))
        elif char.islower():
            results += (chr((ord(char) - (key + 97)) % 26 + 97))
        else:
            results += char
    return results
def caesar_brute_force(ciphertext):
    candidates = []

    shift = range(1,26)

    for key in shift:
        output = caesar_decrypt(ciphertext, key)
        candidates.append((key, output))
    return candidates
if __name__ == "__main__":
    ciphertext = input("What is the ciphertext: ")
    candidates = caesar_brute_force(ciphertext)
    for key, output in candidates:
        print(f"Key: {key} | Decrypted: {output}")
        