import random
import os
import string
import time

path = os.path.dirname(os.path.abspath(__file__))

def clear():
    os.system('cls||clear')

def crypt_file(filename, key, mode):
    source = open(filename, "rb")
    if mode == 'd':
        extension = (source.readline().rstrip()).decode()
    else:
        extension = "xor"
    (name, ext) = os.path.split(filename)[1].split(".")
    target = open(os.path.join(path, name + "." + extension), "wb")
    if mode == 'e':
        ext = ext + "\n"
        target.write(ext.encode())
    data = source.read(len(key))
    while data:
        encrypted = (int.from_bytes(data,"big") ^ int.from_bytes(key.encode(),"big")).to_bytes(len(data), "big")
        target.write(encrypted)
        data = source.read(len(key))
    if mode == 'e':
        print("Encrypted file: " + filename)
    else:
        print("Decrypted file: " + filename)
    source.close()
    target.close()

clear()
mode = input("Press e to encrypt and d to decrypt\n")
while mode != 'e' and mode != 'd':
    clear()
    mode = input("Press e to encrypt and d to decrypt\n")

key = ''

if mode == 'e':
    key_length = input("How long would you like the encryption key to be?\n")
    while not key_length.isdigit():
        key_length = input("How long would you like the encryption key to be? Please enter a number\n")
    key = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(int(key_length)))
    print ("Your key is " + key + "\nPlease remember it")
elif mode == 'd':
    key = input("Please enter your key\n")
source = input("Please enter the name of the file or folder to encrypt\n")
while not os.path.exists(source):
    source = input("File or folder not found. Please try again\n")
if os.path.isfile(source):
    p = os.path.join(path, source)
    crypt_file(p, key, mode)
elif os.path.isdir(source):
    path = os.path.join(path, source)
    for file in os.listdir(source):
        if file.endswith(".xor") and mode == 'd' or not file.endswith(".xor") and mode == 'e':
            p = os.path.join(path, file)
            crypt_file(p, key, mode)
print("Exiting...")
time.sleep(1)
clear()
exit()