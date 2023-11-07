import random

#dictionaire 
dico = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,
        'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17
       ,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

#fonction de décalage à gauche 
def decalage_gauche(m,i):
    n=''
    if i==1:
        while i < len(m):
            n +=m[i]
            i+=1
        n += m[0]
    else :
        while i < len(m):
            n += m[i]
            i += 1
        n +=m[0]
        n +=m[1]
    return n

#fonction de génération de clé DES
def genkey_system_des():
    b = bin(random.getrandbits(64)) #Renvoie un entier de 64 bits
    k = b[2:].zfill(64) #enleve le '0b' et ajoute un 0 au debut pour avoir 64 bit (0b101 va devenir 0101)
    k = str(k)
    k_pc1 = ''
    pc1=[ 57, 49, 41, 33, 25, 17 ,9,
           1, 58, 50, 42, 34, 26, 18,
          10, 2, 59, 51, 43, 35, 27,
          19, 11, 3, 60, 52, 44, 36,
          63, 55, 47, 39, 31, 23, 15,
           7, 62, 54, 46, 38, 30, 22,
          14, 6, 61, 53, 45, 37, 29,
          21, 13, 5, 28, 20, 12, 4
        ]
    #permutation de k suivant pc-1
    for i in pc1:
        k_pc1 += k[i-1]
    #print(f"Permutation de k suivant pc-1 : \n k_pc-1 = {k_pc1}")
    return k_pc1

#fonction de subdivision des partir gauche et droite de la clé principal
def genkey_subkeys_system_des( k_pc1=genkey_system_des()):
    #determination de C0 et D0
    co =k_pc1[:28]
    do =k_pc1[28:]
    print('determination de Cn et Dn avec 1<=n<=16')
    left_shift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    dict_keyc = {0:co}
    dict_keyd = {0:do}
    c , d ,j = co ,do , 1
    for i in left_shift:
        dict_keyc[j] = decalage_gauche(c,i)
        dict_keyd[j] = decalage_gauche(d,i)
        c , d = dict_keyc[j], dict_keyd[j]
        j += 1 
    for i in range(17):
        print(f"c{i}  : {dict_keyc[i]}  , d{i}  : {dict_keyd[i]}")
        pass
    pc2=[14 ,17 ,11 ,24 ,1 ,5
         ,3 ,28 ,15 ,6 ,21 ,10
         ,23 ,19 ,12 ,4 ,26 ,8
         ,16 ,7 ,27 ,20 ,13, 2
         ,41 ,52 ,31 ,37 ,47 ,55
         ,30 ,40 ,51 ,45 ,33 ,48
         ,44 ,49 ,39 ,56 ,34 ,53
         ,46 ,42 ,50 ,36 ,29 ,32
        ]
    s,sp='',''
    keys = []
    #print(f"Permutation de chacune des paires concaténées Cn Dn  suivant pc-2 ")
    for i in range(1,17):
        s = dict_keyc[i] + dict_keyd[i]
        for j in pc2:
            sp += s[j-1]
        keys.append(sp)
        print(f"k{i} = {sp}")
        sp=''
    return keys
