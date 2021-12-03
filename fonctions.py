from random import randint

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
    primes = list_prime(1000)
    p = primes.pop(randint(0,len(primes)-1))
    q = primes.pop(randint(0,len(primes)-1))
    n = p*q #Module de chiffrage
    phiN = (p-1)*(q-1) # Indicatrice d'Euler en n
    e = 2
    while extended_gcd(phiN,e)[0] != 1 and e<phiN:
        e += 1
    if e > phiN:
        raise RuntimeError("LA SAUCE")
    pub = (n,e)
    pgcd,u,v = extended_gcd(e,phiN) # u est la clé privée ?
    print(p,q,phiN,pub,u)
    return pub, u

key_creation()