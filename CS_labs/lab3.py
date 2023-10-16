upper = ['A', 'Ă', 'Â', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Î', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'Ș', 'T', 'Ț', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'ă', 'â', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'î', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'ș', 't', 'ț', 'u', 'v', 'w', 'x', 'y', 'z']


def isLong(key):
    return True if len(key) >= 7 else False

def isValid(key):
    return len(key) >= 7 and all(i in upper or i in lower or i == ' ' for i in key)

def compress(word):
    return ''.join([i.upper() for i in word if i != ' '])

message = input("Enter your desired message: ")
while not isValid(message):
    message = input("Enter your desired message: ")
message = compress(message) 

key = input("Enter your desired key: ")
while (not isValid(key)) and (not isLong(key)):
    key = input("Enter your desired key: ")
key=compress(key) 

while len(key)<len(message):
    key+=key
key= key[:len(message)]


print(message)
print(key)

mess_list = []
key_list = []
for i in message:
    mess_list.append(upper.index(i))
#print(mess_list)

for i in key:
    key_list.append(upper.index(i))
#print(key_list)

def encode():
    encoder = ''
    for i in range(len(message)):
        char = (mess_list[i] + key_list[i]) % 31
        #print(char)
        encoder+=upper[char]
    return encoder

def decode():
    decoder = ''
    for i in range(len(message)):
        char = (upper.index(message[i]) - key_list[i]) % 31
        #print(char)
        decoder+=upper[char]
    return decoder


choice = input("Type e for encryption, d for decryption: ")
if choice == 'e':
    print(encode())
elif choice == 'd':
    print(decode())
else:
    print('Run again')