from random import randint

from numpy.lib.function_base import append

def tests(n):
    '''
    Run n encryption/decryption tests
    '''
    for n in range(n):
        string = ""
        for k in range(randint(1,50)):
            string = string + chr(randint(97,122)) #randint from 97 to 122 (a-z)
        pub, priv = key_creation()
        print(string)
        k = encryption(string,pub)
        print(decryption(k,priv))
        if decryption(k,priv) != string:
            return False
    return True


def list_prime(n):
    liste = []
    for i in range(2,n+1) :
        c = 0
        for j in range(2,i):
            if i % j == 0 :
                break
            if j == i-1:
                liste.append(i)
    return liste

def extended_gcd(a,b):
    """
    Algorithme
    """
    r = 1
    u0,u1,v0,v1 = 1, 0, 0, 1
    while r != 0:
        q,r = a//b, a%b
        if r == 0:
            return b, u1, v1
        else:
            a = b
            b = r
            u2 = u0 - q*u1
            v2 = v0 - q*v1
            u0 = u1
            v0 = v1
            u1 = u2
            v1 = v2

def key_creation():
    flag = True
    while flag: ## pour éviter les problèmes de n < m
        primes = list_prime(1000)
        p = primes.pop(randint(0,len(primes)-1))
        q = primes.pop(randint(0,len(primes)-1))
        n = p*q #Module de chiffrage
        if n > 990: ## max code ascii
            flag = False
    
    phiN = (p-1)*(q-1) # Indicatrice d'Euler en n
    e = 2
    while extended_gcd(phiN,e)[0] != 1 and e<phiN:
        e += 1
    if e > phiN:
        raise RuntimeError("LA SAUCE")
    pub = (n,e)
    pgcd,u,v = extended_gcd(e,phiN) # u est la cle privee
    while u <= 0:
      u+=phiN
    return pub, (n,u)

def convert_msg(msg):
    r = []
    for i in msg:
        if ((i >= 'a' and i <= 'z') or i == ' ') or i=='': #L'enonce demande le chriffrement d'un message sans majuscule, accents ou ponctuation -> pourrait changer
            r.append(ord(i))
        else:
            raise ValueError('On désire seulement chiffrer "une chaîne de caractères ne contenant ni caractère accentué, ni majuscule ni ponctuation"')
    return r

def encryption(msg,key): ##découper en groupe de 4 chiffres et pas 4 lettres
    if type(msg) == str:
        msg_tab = convert_msg(msg)
    else:
        msg_tab = msg
    r = []
    seq = ""
    for m in msg_tab:
        seq = seq + str(m)+"0"*(3-len(str(m)))
    i = 0
    while i < len(seq):
        r.append((int(seq[i:i+3])**key[1])%key[0])        
        i += 3
    #r = (ord(msg[0])**key[1])%key[0]
    return r

def decryption(msg,key):
    r = ""
    for m in msg:
        m = str((m**key[1])%key[0])
        if (m[2] == '0') and (m[0] > '1'): #On vérifie si le nombre est de forme est 9X0 ou 3X0 (ASCII 2 chiffres), la table ascii ne dépasse pas 127 de toute manière
            m = m[0:-1]
        #print(m +" = "+ chr(int(m)))
        r = r + chr(int(m))
    return r