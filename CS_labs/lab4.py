#task 2.5
k_plus = "1111000 0110011 0010101 0101111 0101010 1011001 1001111 0001111"
c = ''
d = ''
cd=[]
left_shift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

pc_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]


def c_d(key, c, d):
    for i in key:
        if i != " " and len(c)<28:
            c+=i
        elif i != " ":
            d+=i
    return c,d

def lss(j):
    j +=j[0]
    j = j[1:]
    return j

def shifter(ls, cd):
    for j in range(16):
        c = cd[j][0]
        d = cd[j][1]
        for i in range(ls[j]):
            c = lss(c)
            d = lss(d)
        cd.append([c,d])
    return(cd)

def perm(pc_2, cd):
    k = []
    for j in range(17):
        cdn = cd[j][0]+cd[j][1]
        key =''        
        for i in range(len(pc_2)):
            key+=cdn[(pc_2[i])-1]
        k.append(key)
    return k

        




c,d = c_d(k_plus,c,d)
cd.append([c,d])
cd = shifter(left_shift,cd)
k = perm(pc_2, cd)
k.pop(0)
print(k)
