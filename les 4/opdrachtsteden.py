#maak een lijst met steden in kies er en random 3 via random module op de index indien de index even is vervang je de naam door streepjes indien de index oneven is door steretjes
#print de lijst af waarbij de vervanging is doorgegeven 
import random
steden =["antwerpen", "brussel", "gent", "leuven", "brugge", "kortrijk", "bornem", "mechelen"]
alle_index = []

while len(alle_index)<3:
    niewe_index = random.randint(0,len(steden)-1)
    if niewe_index not in alle_index:
        alle_index.append(niewe_index)

print(alle_index)

index = 0
for stad in steden:
    if index %2 == 0 and index in alle_index:
        print('-'*len(stad))
    elif index %2 != 0 and index in alle_index:
        print('*'*len(stad))
    else:
        print(stad)
    index+= 1
