import numpy as np
import random
import matplotlib.pyplot as plt
import time

start_time=time.time()

def lancio():
    return random.randrange(1,7)

counter=1
list=[]
check=[0,0,0,0,0,0]
histo=[]
flag=False

for i in range(10000):

        #while(all(check)==False):
        while not flag:
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
            
            if (check[0]==False and list.count(1)==list.count(2)==list.count(3)==list.count(4)==list.count(5)):
                check[0]=counter
                
            elif (check[1]==False and list.count(2)==list.count(3)==list.count(4)==list.count(5)==list.count(6)):
                check[1]=counter
                
            elif (check[2]==0 and list[0]==list[1]==list[2]==list[3]==list[4]):
                check[2]=counter
                
            elif (not check[3] and (list.count(1)==4 or list.count(2)==4 or list.count(3)==4 or list.count(4)==4 or list.count(5)==4 or list.count(6)==4)):
                check[3]=counter
                
            elif (check[4]==0 and list[0]==list[1]==list[2]):
                if(list[3]!=list[4] and list[3]!=list[2]):
                    check[4]=counter
                    
            elif(check[4]==0 and list[2]==list[3]==list[4]):
                if(list[0]!=list[1] and list[1]!=list[2]):
                    check[4]=counter
                        
            elif(check[4]==0 and list[1]==list[2]==list[3]):
                check[4]=counter
                    
            elif (check[5]==0 and list[0]==list[1]==list[2]):
                if(list[3]==list[4] and list[3]!=list[2]):
                    check[5]=counter
                        
            elif (check[5]==0 and list[2]==list[3]==list[4]):
                if(list[0]==list[1] and list[1]!=list[2]):
                    check[5]=counter
                            
                            
            #print("{0}.\t{1}".format(counter,list))
        
                
            if(all(check)!=False):
               flag=True

            list.clear()
            counter+=1
 
        
        print("Numero lanci necessari per la prima condizione: {0}\nNumero lanci necessari per la seconda condizione: {1}\nNumero di lanci necessari per tutti uguali: {2}\nNumero di lanci necessari per il poker: {3}\nNumero di lanci per il tris: {4}\nNumero di lanci per il full: {5}".format(check[0],check[1],check[2],check[3],check[4],check[5])) 

        print("Numero di lanci necessari per il tutto: {0}".format(counter-1))
        check=[0]*6
        histo.append(counter-1)
        counter=1
        flag=False
        print("\n\n")





n,bins,patches=plt.hist(histo,bins=len(set(histo)),facecolor="green")
plt.savefig("IstogrammaKNIFFEL")





print("Tempo di esecuzione: ",time.time()-start_time)

