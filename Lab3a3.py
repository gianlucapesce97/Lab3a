import random as rand
import time
import matplotlib.pyplot as plt


#Assegniamo 1->C  , 2->L ,  3->R  ,  456  -> .


def setup():
    
    coins={ 
        0:20,
        1:20,
        2:20,
        3:0
    }

    return coins,0,False,0



def check_and_roll (player,tot_players,coins):
    roll=rand.randint(1,6)

    if(roll<4):
        coins[player]-=1
        if(roll==1):
            coins[tot_players]+=1
        elif(roll==2):
            coins[(player-1)%tot_players]+=1
        else:
            coins[(player+1)%tot_players]+=1

        


def main():


    N=1000
    start=time.time()
    dist=list()
    
    

    for i in range (0,N):
    
        coins,rounds,winner,player=setup()
        tot_players=len(coins)-1
    
        
        while not winner:
            
            
            if coins[player]>2:
                rolls=3
            else:
                rolls=coins[player]

            for v in range(rolls):
                check_and_roll(player,tot_players,coins)
                
                end=set(coins.items()) & set(list(filter(lambda x: x[1] and x[0] !=3, coins.items())))
                if len(end)==1:
                   winner=True

                #if((coins[0]==0 & coins[1]==0) or (coins[0]==0 & coins[2]==0) or (coins[1]==0 & coins[2]==0)):
                   # winner=True
       
      

            rounds+=1
            player=(player+1)%tot_players 
        
        dist.append(rounds)
            

    print("Runtime: %.3f" % (time.time() - start))
    print('# min di rounds:',min(dist),'\n# max di rounds: ',max(dist),'\nMedia dei rounds:', sum(dist)/len(dist))
    n,bins,patches=plt.hist(dist,bins=len(set(dist)),facecolor="red")
    plt.savefig("IstogrammaCLR")
    plt.close()

if __name__=='__main__':
    main()

                        
                        
                        
                        



        
            
            
        
                
                
                
    








