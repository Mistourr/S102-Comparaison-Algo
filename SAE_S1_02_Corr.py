import numpy as np

def vector_set(display=False): ## Preuve de la Q2.2
    vectors = [
    np.array([1,0,0,0]),
    np.array([0,1,0,0]),
    np.array([0,0,1,0]),
    np.array([0,0,0,1])
    ]
    result = [] #Ensemble F4²
    result.append(np.array([0,0,0,0])) ## Vecteur nul qui appartient forcément à F4²
    for i in range(len(vectors)):
        result.append(vectors[i])
        for j in range(i+1,len(vectors)):
            result.append(vectors[i]+vectors[j])
            for k in range(j+1,len(vectors)):
                result.append(vectors[i]+vectors[j]+vectors[k])
                for v in range(k+1,len(vectors)):
                    result.append(vectors[i]+vectors[j]+vectors[k]+vectors[v])
    if display:
        for el in result:
            print(el)
        print("card :",len(result))
    return result

def im(vecs): # Preuve Q2.3
    '''
    retourne l'ensemble des images de applicationMatrice() par vecs -> on donne donc F4² en paramètre
    '''
    image = []
    for i in vecs:
        image.append(application_matrice(i)%2)
    return image

def application_matrice(vec):
    '''
    Réplique l'application linéaire pour les vecteurs de 4 bits à l'aide de la matrice de l'application linéai  re.
    '''
    m = np.array(
        [
        [1,1,0,1],
        [1,0,1,1],
        [1,0,0,0],
        [0,1,1,1],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]
        ]
    )
    return np.matmul(m,vec)%2

def antecedent(vec):
    '''
    Retrouve l'antécédent d'une image
    '''
    vecset = vector_set()
    for v in vecset:
        if np.array_equal(application_matrice(v),vec):
            return v
    return np.array([0,0,0,0])
def poids(vec):
    count = 0
    for i in vec:
        if i == 1:
            count += 1
    return count

def checkQ24(): ## Preuve Q2.4
    vecset = vector_set()
    image = im(vecset)
    for i in image:
        for j in image:
            if np.array_equal(i,j):
                continue
            if poids((i+j)%2) < 3:
                print("La distance entre",i,"et",j,"est inférieur à 3")
                return
    print("Toute les combinaisons possibles de u et v donnent d(u,v) >= 3")
    return

def checkQ25():
    image = im(vector_set())
    for vecU in image:
        for bit in range(len(vecU)):
            vecUdiff = np.copy(vecU)
            vecUdiff[bit] = (vecUdiff[bit]+1)%2
            for vecV in image:
                if np.array_equal(vecV,vecU):
                    continue
                if poids((vecU+vecUdiff)%2) > poids((vecU+vecV)%2):
                    return "La distance entre u et ~u est plus grande qu'entre u et v !"
    return "La distance entre u et ~u est toujours la plus petite !"

def debruiter(vec):
    image = im(vector_set())
    r = image[0]
    for u in image:
        if poids((vec+u)%2) < poids((vec+r)%2):
            r = u
    return r
