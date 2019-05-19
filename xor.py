import string
import random



def str_xor(s1, s2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1, c2) in zip(s1, s2)])
def encryption(message, key):
    
    enc = str_xor(message, key)
    file = open("Message.txt",'w')
    file.write(enc)
    file.close()

def decrypt(key):
    file = open("Message.txt",'r')
    enc = file.read()
    return str_xor(enc, key)

def main():
    choice = input("Do you want to encrypt or decrypt a message.(D|E): ")
    if choice == 'd' or choice == 'D':
        file = input("Enter key File: ")
        key = open(file, 'r')
        k = key.read()
        key.close()
        
        dmessage = decrypt(k)
        print(dmessage)
    if choice == 'e' or choice == 'E':
        key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase +
                            string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0,1024))
        kFile = open("key" + random.digit() + ".txt", 'w')
        kFile.write(key)
        kFile.close()
        
        message = input('Enter the message: ')
        
        messFile = open("notMessage.txt", 'w')
        messFile.write(message)
        messFile.close()
        
        encryption(message, key)
if __name__ == '__main__':
    main()
    
        
        
