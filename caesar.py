ciphertext = input("What is the ciphertext: ")
key = int(input("What is the key: "))
plaintext = ""
for char in ciphertext:
    if char.isupper():
        plaintext +=(chr((ord(char) - (key + 65))%26 +65))
    elif char.islower():
        plaintext +=(chr((ord(char)-(key + 97))%26 +97))
    else:
        plaintext +=(char)
print(f"The plaintext is: {plaintext} ")