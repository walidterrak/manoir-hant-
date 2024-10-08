from random import randint
print("Le manoir hanté du DR. Walid")

je_suis_un_bonhomme=True
score=0
while je_suis_un_bonhomme:
    porte_fantome=randint(1,3)
    print("tu entend des bruit bizzard dans le manoir...")
    print("tu est devant trois portes...")
    print("laquelle ouvre tu ?!")
    porte=input	("1,2 ou 3 ?")
    num_porte= int(porte)
    if num_porte == porte_fantome:
        print(" UN FANTOME !!")
        je_suis_un_bonhomme=False
    else:
        print("pas de fatome... pour linstant.")
        print("tu avance dans la prochaine salles")
        score=score + 1
print("au secour !")
print("partie terminée ! ton score est de :", score)