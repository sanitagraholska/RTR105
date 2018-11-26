# Fails : 170.py
# Autors : Sanita Graholska
# Apliecibas numurs : 181REB311
# Datums : 26.11.2018
# Sagatave funkcijas saknes meekleshanai ar dihatomijas metodi

# -*- coding: utf -8 -*-
from math import sin, fabs
from time import sleep

def f(x):
    return sin(x)

# Definejam argumenta x robezhas :
a = 1.1
b = 3.2

# Aprekjinam funkcijas x robezhas :
funa = f(a)
funb = f(b)

# Paarbaudam , vai dotajaa intervaalaa ir saknes :
if ( funa * funb > 0.0 ):
    print "Dotajaa intervaalaa [%s, %s] saknju nav"%(a,b)
    sleep(1); exit()    # Zinjo uz ekraana, gaida 1 sec. un darbu pabeidz
else:
    print "Dotajaa intervaalaa sakne (s) ir!"

# Defineejam precizitaati, ar kaadu mekleesim sakni :
deltax = 0.01

# Sashaurinam saknes mekleeshanas robezhas :
while (fabs(b-a) > deltax ):
    x = (a+b)/2; funx = f(x)
    if ( funa*funx < 0. ):
        b = x
    else :
        a = x

print "Sakne ir : ", x
