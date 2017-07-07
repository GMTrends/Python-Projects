from sense_hat import SenseHat
sense = SenseHat() # SenseHat object creation
from time import sleep

# Step 8: Write a function named total_sales_function that takes  four parameters: a dictionary, the price of an early bird  ticket, the price of a matinee ticket, and the price of an  evening ticket.  
# Create a dictionary tickets_dict.  Use a  loop to multiply the price of each type of ticket by the  number of tickets sold.  Store the key and the result of  the calculation in the tickets_dict.  
# Return the  tickets_dict	  
def total_sales_function(movie_tickets_sold,early_bird_price,matinee_price,evening_price):
  tickets_dict = {}
  for key, value in movie_tickets_sold.items():
    if key == "Early Bird":
      tickets_dict[key] = (float(value) * float(early_bird_price))
    elif key == "Matinee":
      tickets_dict[key] = (float(value) * float(matinee_price))
    elif key == "Evening":
      tickets_dict[key] = (float(value)) * (float(evening_price))
  return tickets_dict

def main():
  # Step 1: Create a dictionary named tickets_sold_dict
	tickets_sold_dict = {}
	ticket_str = input("Enter a movie name - key\n")
	
	# Step 2: Write a loop to prompts user to input keys and values and store them in tickets_sold_dict
	while ticket_str != "exit":
	  
	  ticket_amount = int(input("Enter the amount of ticket sold\n"))
	  tickets_sold_dict[ticket_str.lower()] = ticket_amount
	  ticket_str = input("Enter a movie name;exit\n")
	
	# Step 3: Use the keys function to access the keys in tickets_sold_dict
	print("keys")
	for key in tickets_sold_dict.keys():
	  #a dict_key object is returned
	  print("movie name", key)
	 
	# Step 4: Use the values function to access the values in tickets_sold_dict 
	for value in tickets_sold_dict.values():
	  #a dict_key object is returned
	  print("movie name", value) 
	  
	# Step 5: Compute the sum of all of the values for the tickets sold.  Print out the sum.
	
	cost = sum(tickets_sold_dict.values())
	print("cost of all items ", str(cost))
	
	# Step 6: Create a dictionary named movie_tickets_dict and assign these values for the number of tickets sold.
	movie_tickets_dict = {'Early Bird':511,'Matinee':343,'Evening':942}
	  
	# Step 7: Write a loop which allows the user to enter a key to search for in the movie_tickets_dict
	try:
	  find = input("Enter a key to find")
	  if find in movie_tickets_dict:
	    print("number of tickets is ", str(movie_tickets_dict[find]))
	  else:
	    print("The search key was not found")
	    print("access an item which has no key")
	    print("exception ", str(movie_tickets_dict[find]))
	except KeyError:
	  print("Error, key not in dictionary")
	  
	
	# Step 9: Call the function from within main with the following arguments.
	tickets_cost_dict = total_sales_function(movie_tickets_dict, 4.00, 5.50, 6.25)
	print("")
	for item, price in tickets_cost_dict.items():
	  print("Showtime: " + item + ". Price " + format(price,'0.2f'))
	print("")

	#Step 10: Use SenseHat to obtain variable values to create dictionary
	sense_hat_dict = {"temperature":sense.get_temperature(), "pressure":sense.get_pressure(),\
                "humidity":sense.get_humidity(),"position":sense.get_orientation(),\
                "acceleration":sense.get_accelerometer_raw()}
				  
	for key, value in sense_hat_dict.items():
		print("")
		print(key, value)
	print("")
	
	#Step 11: Print out the keys and values for each item in dictionary
	for key in sense_hat_dict.keys():
    if isinstance(sense_hat_dict[key],float):
      print("\nValue is a float --> " + format(sense_hat_dict[key],'0.2f'))     
    if isinstance(sense_hat_dict[key],dict):
      print("\nValue is a dictionary")
      item_dict = sense_hat_dict[key]
      for key,value, in item_dict.items():              
        print("key = " + key + ". value = " + str(value))

main()
	 