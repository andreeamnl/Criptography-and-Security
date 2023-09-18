upper= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
space = ' '
digits = list(range(1, 26))
x = input('Enter phrase: ')


def isValid(x):
    flag = True
    for i in x:
        if (i not in upper) and(i not in lower) and (i not in space):
            print(i)
            print(f"You can't use '{i}'")
            flag = False
            break
    return flag


def compress(x):
    phrase = ''
    for i in x:
        if i.islower():
            phrase +=i.upper()
        elif i.isupper():
            phrase+=i
    return phrase



key2 = input('Enter textual key: ')

def isValid2(x):
    flag = True
    if len(x)<7:
        flag = False
    for i in x:
        if (i not in upper) and(i not in lower) and (i not in space):
            print(i)
            print(f"You can't use '{i}'")
            flag = False
            break
    return flag


def compresser2(key2):
    compressed = ''
    for letter in key2:
        if (letter.upper() not in compressed):
            compressed+=letter.upper()
            #print(f"letter is {letter} compressed is {compressed}")
    return compressed



while not isValid2(key2):
    key2 = input("Try again: ")
key2 = compresser2(key2)
print(key2)





def new_upper():
    list = []
    lister = [i for i in key2]
    list+= lister
    #print(list)
    for i in upper:
        if (i not in list):
            list.append(i)
    return list

new_upper_list = new_upper()
print("New alphabet provided bwelow:")
print(new_upper_list)


def change_index_encryption(letter, key):
    new_index = 0
    #print(f"letter is {letter}, key is {key}")
    current_index = upper.index(letter)
    new_index = current_index+key
    #print(f"new index is {new_index}")
    if new_index>25:
        new_index =  new_index - 26
    return new_index

def change_index_decryption(letter, key):
    new_index = 0
    #print(f"letter is {letter}, key is {key}")
    current_index = new_upper_list.index(letter)
    new_index = current_index-key
    if new_index<0:
        new_index = 26 + new_index
    return new_index


def encrypt(x):
    #print(f"youre in encrypt , x is {x}")
    encrypted = ''
    for i in x:
        encrypted += new_upper_list[change_index_encryption(i,key)]
    return encrypted


def decrypt(x):
    #print(f"youre in decrypt , x is {x}")
    decrypted = ''
    for i in x:
        decrypted += upper[change_index_decryption(i,key)]
    return decrypted


###################################

while not isValid(x):
    x = input("Try again: ")
x = compress(x)



key = int(input("Enter a valid key: "))
while key not in digits:
    key = int(input("Try entering a valid digit 1-9 : "))
print(f"key is {key}")

choice = input("Type e for encryption, d for decryption: ")
if choice == 'e':
    print(encrypt(x))
elif choice == 'd':
    print(decrypt(x))
else:
    print('Run again')
