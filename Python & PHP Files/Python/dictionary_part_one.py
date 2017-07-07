#dictionary_part_one.py
#Entering a new price will overwrite the original values

#Keys -> Keys can be string, integer, tuples.  Keys are immutables
#Values -> float, integer, string, list, dictionary, class

def main():
    components_dict = {'capacitor':0.89,'LED':1.34}
    comp_str = input("Enter a new component - key\n")
    while comp_str != "exit":
        comp_price = float(input("Enter the price\n"))
        components_dict[comp_str.lower()] = comp_price
        comp_str = input("Enter a new component;exit\n")

    print(components_dict)

    print("key and value")
    for key,value in components_dict.items(): #returns key:value
        print("component name", key, " price", value)

    print("keys")
    for key,value in components_dict.keys(): #a dict_key object is returned
        print("component name", key)

    print("values")
    for key,value in components_dict.values(): # a dict_value object is returned
        print("component name", price)

    cost = sum(components_dict.values())
    print("cost of all items ", str(cost))

    try:
        find = input("Enter a key to find")
        if find in components_dict:
            print("value is ", str(components_dict[find]))
        else:
            print("key not found")
            print("access an item which has no key")
            print("exception ", str(components_dict[find]))
    except KeyError:
        print("Error key not in dictionary")
        

main()
