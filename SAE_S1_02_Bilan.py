import numpy as np
from numpy.lib.function_base import meshgrid
from SAE_S1_02_RSA import *
from SAE_S1_02_Corr import *

def noise(vect_msg):
    """
    prend un vecteur vect_msg et renvoie ce vecteur potentiellement bruite
    """
    ### on fait une copie du vecteur initial
    vect = vect_msg.copy()
    ### une chance sur quatre de ne pas bruiter le vecteur
    test = np.random.randint(0,4)
    if test>0:
        index = np.random.randint(0,np.size(vect))
        vect[index] = (vect[index] +1)%2
    return vect

def convert_msg_to_bin(msg):
    return [bin(i) for i in msg]

def num_to_vec(num):
    '''
    Transfome un chiffre en vecteur binaire de 4bits
    '''
    r = []
    for i in range(4):
        r.append(num//(2**(3-i)))
        num %= 2**(3-i)
    return np.array(r)

def vec_to_num(vec):
    '''
    Transforme un vecteur binaire de 4bits en chiffre
    '''
    r = 0
    for i in range(4):
        r += vec[i]*(2**(3-i))
    return r

def binary_words(num):
    '''
    Transforme un nombre en plusieurs vecteurs de 4bits,
    un par chiffre du nombre.
    '''
    num_str = str(num)
    return [ num_to_vec(int(x)) for x in num_str ]

def words_to_number(words):
    '''
    Transforme une liste de vecteurs binaires de 4bits vers un nombre décimale
    '''
    s = ''
    for word in words:
        s = s + str(vec_to_num(word))
    return int(s)

def transmit(msg):
    r = []
    for word in msg:
        r.append([noise(application_matrice(lettre)) for lettre in word])
    return r

def denoising(msg):
    r = []
    for word in msg:
        r.append([debruiter(lettre) for lettre in word])
    return r

def recompose_msg(msg):
    '''
    Recompose un message sous forme de liste de nombres à l'aide d'une liste de liste de mots/vecteurs binaires
    '''
    r = []
    for word in msg:
        r.append([antecedent(letter) for letter in word])
    return r

pub,priv = key_creation() # création des clés
print("clé publique :",pub,"\nclé privé :",priv,"\n")
msg = input("Tapez le message à envoyer : ")
msg = convert_msg(msg)
print("\nMessage en nombres :",msg,"\n")
msg = encryption(msg,pub)
print("Message encrypté:",msg,"\n") ## 4 bits par message à passer par l'application pour en obtenir 7
msg = [binary_words(x) for x in msg] ## on créer un tableau contenant des tableaux pour chaque mot en binaire
print("Traduction en binaire :",msg,"\n")
msg = transmit(msg)
print("Message reçu bruité :",msg,"\n")
msg = denoising(msg)
print("Message débruité :",msg,"\n")
msg = recompose_msg(msg)
print("Message recomposé sur ses 4bits:",msg,"\n")
msg = [words_to_number(word) for word in msg]
print("Message en nombres chiffrés :",msg,"\n")
msg = decryption(msg,priv)
print("Message reçu déchiffré :",msg,"\n")