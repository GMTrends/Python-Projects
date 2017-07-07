#dictionary_functions_part_two.py

def compute_discount(original_dict, mark_down_percent):
    sales_price_dict = {}  #create a new dictionary
    for key in original_dict.keys():
        sales_price_dict[key] = original_dict[key] * (1 - mark_down_percent)
    return sales_price_dict

def main():
    grocery_dict = {"beets":3.45,"carrots":4.50,"kolrabi":6.99}

    new_item = input("Enter a new vegetable: ")
    while new_item.lower() != "exit":
        price_each = float(input("Enter the price each: "))
        grocery_dict[new_item] = price_each
        new_item = input("Enter a new vegetable; exit ")

    updated_dict = compute_discount(grocery_dict,0.05) #Call the discount function

    print("\ngrocery_dict")
    for item_name,price in grocery_dict.items():
        print("item " + item_name + " price " + format(price,'0.2f'))

    print("\nupdated_dict")
    for item_name,price in updated_dict.items():
        print("item " + item_name + " price " + format(price,'0.2f'))

    print("\ntotal for all items $" + format(sum(grocery_dict.values())))
    print("minimum cost of an item $" + str(min(grocery_dict.values())))
    print("maximum cost of an item $" + format(max(grocery_dict.values())))

    max_cost = 0.0
    max_item = ""
    for item_name,price in grocery_dict.items():
        if price > max_cost:
            max_cost = price
            max_item = item_name
    print("\nThe most expensive item is " + max_item)
    print("\ntotal number of items " + str(len(grocery_dict)))

    #Go through the list to check if an item is in it.
    #Prompt user to delete an item..
    item_to_delete = input("\nEnter a grocery item to delete: ")
    if item_to_delete in grocery_dict:
        print("\nitem found")
        #del(grocery_dict[item_to_delete]))
        item_removed = grocery_dict.pop(item_to_delete)
        if item_removed != None:
            print("after deleting an item value = " + str(item_removed))
        for item_name,price in grocery_dict.items():
            print("item " + item_name + " price " + format(price,'0.2f'))
    else:
        print("item not found")

    
    
main()


