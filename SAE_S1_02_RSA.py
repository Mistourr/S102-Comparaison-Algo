from random import randint

def list_prime(n):
    '''
    Liste tous les nombres premiers de 2 à n
    '''
    liste = []
    for i in range(2,n+1):
        for j in range(2,i): ## On aurait pu utiliser jusqu'à racine carré de i mais plus le temps de recoder ...
            if i % j == 0 : ## Si j divise i alors on passe au prochain i car il n'est pas premier
                break
            if j == i-1: ## Si il passe tous les j alors on l'ajoute au résultat
                liste.append(i)
    return liste

def extended_gcd(a,b):
    """
    Algorithme d'Euclide étendu
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
    while extended_gcd(phiN,e)[0] != 1 and e<phiN: ## On cherche un e tel que e est premier avec phiN et e est inférieur à phiN
        e += 1
    if e > phiN: ## Si jamais ça arrive mais normalement non
        raise RuntimeError("e ne devrait pas être supérieur à phiN")
    pub = (n,e)
    pgcd,u,v = extended_gcd(e,phiN) # u est la cle privee
    while u <= 0: ## Si u est négatif on ajoute des phiN car ils sont "annulés" par le modulo
      u+=phiN
    return pub, (n,u)

def convert_msg(msg):
    '''
    Convertit un message en liste de codes ASCII
    '''
    r = []
    for i in msg:
        r.append(ord(i))
        
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
    return r

def decryption(msg,key):
    r = ""
    for m in msg:
        m = str((m**key[1])%key[0])
        if (m[2] == '0') and (m[0] > '2'): #On vérifie si le nombre est de forme est 9X0 ou 3X0 (ASCII 2 chiffres), la table ascii ne dépasse pas 127 de toute manière
            m = m[0:-1]
        r = r + chr(int(m))
    return r