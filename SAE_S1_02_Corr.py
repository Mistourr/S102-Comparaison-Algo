import numpy as np
from numpy.core.defchararray import count
from numpy.lib.function_base import disp

def vector_set(display=False): ## Preuve de la Q2.2
    vectors = [
    np.array([1,0,0,0]),
    np.array([0,1,0,0]),
    np.array([0,0,1,0]),
    np.array([0,0,0,1])
    ]
    result = [] #Ensemble F4²
    result.append(np.array([0,0,0,0])) ## Vecteur nulle qui appartient forcément à F4²
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

def im(vecs):
    '''
    retourne l'ensemble des images de applicationMatrice() par vecs -> on donne donc F4² en paramètre
    '''
    image = []
    for i in vecs:
        image.append(applicationMatrice(i))
    for k in image: ## Sanitize 1 and 0
        for v in k:
            v
    return image


def applicationMatrice(vec):
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
    return np.matmul(m,vec)

def poids(vec):
    count = 0
    for i in vec:
        if i > 0:
            count += 1
    return count