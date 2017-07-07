#listtwo.py
from sense_hat import SenseHat
from time import sleep

def main():
    sense = SenseHat()
    temps_list = [0]*5
    count = 0
    while count < len(temps_list):  #Create an array with 5 elements in it
        temps_list[count] = sense.get_temperature()
        count += 1

    for index in range(0,len(temps_list)):
        print(temps_list[index])

    temps_list2 = [98.6,32,212.0,37]
    print("Sum " + str(sum(temps_list2)))  #Sums up all the elements
    print("Minimum " + str(min(temps_list2))) #Find the minimum
    print("Maximum " + str(max(temps_list2)))  #Find the maximum

    print("Concatenating lists")
    longer_list = temps_list + temps_list2
    for i in range(0,len(longer_list)):
        print(longer_list[i])

    try:
          index2 = input("Enter the index")
          index2 = int(index2)
          print("Your selection " + str(temps_list2[index2]))
    except IndexError:
          print("Your index was out of range")

    course_list = ['cop2334','cop2800','cop1030','cop2360','cop2805','cop2840']

    #Slicing demonstration: cut off part of the array
    print(course_list[2:4])     #start point is course_list[1]end point is course_list[3]
    print(course_list[:3])      #end point is course_list[2]
    print(course_list[8:])      #start point is course_list[7]
    print(course_list[2:])      #start point is course_list[1]

    while True:
        print("Original course_list")
        for c in course_list:   #foreach
            print(c)

        try:
            course_name = input("Enter a course to remove")
            course_list.remove(course_name)  #remove item from the list
        except ValueError:
            print(course_name + " is not in the list")
            break

        print("Updated course_list")
        for c in course_list:   # foreach
            print(c)

    del(course_list[0])
    print("Updated course_list after del")
    for c in course_list:       # foreach
        print(c)
        

main()
