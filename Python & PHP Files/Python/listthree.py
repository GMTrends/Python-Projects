#listthree.py
from sense_hat import SenseHat
from time import sleep

def main():
    cities = ['Miami','Port au Prince','Fort Lauderdale','Montego Bay']
    
    cities.sort()   #Sort into numeric/alphabetic order
    print("Sorted in order")
    for c in cities:
        print(c)
        
    cities.reverse()
    print("\nSorted in reverse order") #Sort in reverse alphabetic/numeric order
    for c in cities:
        print(c)

    tropical_cities = cities    #Adds a pointer (only) to the original list
    for t in tropical_cities:
        print(t)

    print("\nCities list")
    cities.append('Paris')
    for t in tropical_cities:
        print(t)

    #deep copy to an empty list
    tropical_cities_2 = []
    for i in range(0,len(cities)):  
        tropical_cities_2.append(cities[i])

    tropical_cities_2.append('Rio de Janeiro')
    print("\nCities list")
    for c in cities:
        print(c)
    print("\nTropical_cities_2 list")
    for c in tropical_cities_2:
        print(c)

    #deep copy to a list
    tropical_cities_3 = ['none']*len(cities)    
    for i in range(0,len(cities)):
        tropical_cities_3[i] = cities[i]

    tropical_cities_4 = [] + tropical_cities  #deep copy to a list
    tropical_cities_4.append('Lake Worth')
    print("Cities list")
    for c in cities:
        print(c)
    print("\nTropical_cities_4 list")
    for c in tropical_cities_4:
        print(c)
    

main()
