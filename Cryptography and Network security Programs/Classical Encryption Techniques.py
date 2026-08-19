import string


def caesar_cipher(text,shift):
    result=""
    for ch in text:
        if ch.isalpha():
            result+=chr((ord(ch)-65+shift)%26+65)
        else:
            result+=ch
    return result


def generate_key(text,key):
    key=key.upper()
    new_key=" "
    j=0
    for ch in text:
        if ch.isalpha():
            new_key+=key[j%len(key)]
            j+=1
        else:
            new_key+=ch
    return new_key


def vigenere_cipher(text,key):
    key=generate_key(text,key)
    cipher=""
    for p,k in zip(text,key):
        if p.isalpha():
            cipher+=chr((ord(p)+ord(k)-130)%26+65)
        else:
            cipher+=p
    return cipher


def rail_fence_encrypt(text,rails):
    fence=[' 'for _ in range(rails)]
    row=0
    direction=1
    for ch in text:
        fence[row]+=ch
        if row==0:
            direction=1
        elif row==rails-1:
            direction=-1
        row+=direction
    return ''.join(fence)

plain=string.ascii_uppercase
key="QWERTYUIOPASDFGHJKLZXCVBNM"
table=dict(zip(plain,key))

def mono_encrypt(text):
    cipher=""
    for ch in text:
        if ch.isalpha():
            cipher+=table[ch]
        else:
            cipher+=ch
    return cipher

plaintext=input("Enter Plaintext:").upper()

#Caesar Cipher
shift=3
caesar=caesar_cipher(plaintext,shift)

#Vigenere Cipher
keyword="LEMON"
vigenere=vigenere_cipher(plaintext,keyword)

#Rail Fence
rails=3
rail=rail_fence_encrypt(plaintext,rails)

#MonoAlphabetic
mono=mono_encrypt(plaintext)

print("\n============Sample Output/Result===========\n")
print("Plaintext:",plaintext)
print("\nCaesar Cipher:")
print("Shift key:",shift)
print("Ciphertext:",caesar)
print("\nVigenere Cipher:")
print("Keyword:",keyword)
print("Ciphertext:",vigenere)
print("\nRail Fence Cipher:")
print("Rails:",rails)
print("Ciphertext:",rail)
print("\nMonoalphabetic Cipher:")
print("Key:",key)
print("Ciphertext:",mono)
print("\n============================================\n")
print("Frequency Analysis")
print("{:<20}{}".format("Cipher","Resistance"))
print("-"*35)
print("{:<20}{}".format("Caesar Cipher", "Very Low"))
print("{:<20}{}".format("Rail Fence", "Low"))
print("{:<20}{}".format("Monoalphabetic", "Medium"))
print("{:<20}{}".format("Vigenere Cipher", "High"))
