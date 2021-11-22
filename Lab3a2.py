import math
import numpy as np
import random
import matplotlib.pyplot as plt


def lancio():
    return random.randrange(1,7)

list=[]
counter1=0
counter2=0
counter3=0
counter4=0
counter5=0
counter6=0
for i in range (100000):
    dado1=lancio()
    dado2=lancio()
    dado3=lancio()
    dado4=lancio()
    dado5=lancio()
    list.append(dado1)
    list.append(dado2)
    list.append(dado3)
    list.append(dado4)
    list.append(dado5)
    list.sort()

    if(list.count(1)==list.count(2)==list.count(3)==list.count(4)==list.count(5)):
        counter1+=1
    
    elif(list.count(2)==list.count(3)==list.count(4)==list.count(5)==list.count(6)):
        counter2+=1
    
    elif(list[0]==list[1]==list[2]==list[3]==list[4]):
        counter3+=1

    elif(list.count(1)==4 or list.count(2)==4 or list.count(3)==4 or list.count(4)==4 or list.count(5)==4 or list.count(6)==4):
        counter4+=1

    elif(list[0]==list[1]==list[2]):
        if(list[3]!=list[4]):
            counter5+=1
        else:
            counter6+=1
    
    elif(list[2]==list[3]==list[4]):
        if(list[0]!=list[1]):
            counter5+=1
        else:
            counter6+=1

    elif(list[1]==list[2]==list[3]):
        counter5+=1

    else:
        pass


    #print(list)
    list.clear()
    
    

print("Numero di volte 12345: {0}\nNumero di volte 23456: {1}\nNumero di volte tutti uguali: {2}\nNumero di Poker: {3}\nNumero di Tris: {4}\nNumero di Full: {5}".format(counter1,counter2,counter3,counter4,counter5,counter6))


