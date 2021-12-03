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
    return