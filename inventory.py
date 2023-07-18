# Class Shoes
class Shoes:
    
    
    
    # Initialise attributes
    def __init__(self,country,code,product,cost,quantity):
        
     self.country = country
     self.code = code
     self.product  =product
     self.cost = cost
     self.quantity = quantity   
    
    
    
    # Define methods
    def get_cost(self):
      return self.cost
  
  
    def get_quantity(self):
      return self.quantity
  

    def __str__(self):
      return f" Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"
  
  
# Empty shoe_list
shoe_list=[]



# Define function
# Open/read lines in file
# Create shoe object 
# Append to shoe_list
# Try/Except for error handling
def read_shoe_data():
     try:
            
            with open("inventory.txt","r") as file:
                file_data = file.readlines()
                
                
                
                
                for line in file_data[1:]:
                    line = line.split(",")
                    
                    
                    
                    item_data = Shoes(line[0],line[1],line[2],line[3],line[4])
                    
                    
                    
                    shoe_list.append(item_data)
                    
            
     except FileNotFoundError as error:
            print(error)
            
            print("This file was not found, please try again.")
            
          
    

     
# Define function
# Capture data about a shoe
# Create shoe_object
# Append shoe_object to shoe_list 
# Open/Write in text file   
def capture_shoes():
    
       
        
    
        country = input("Please enter the country:\n")
        code = input("Please enter the code:\n")  
        product =input("Please enter the product:\n") 
        cost = int(input("Please enter the cost:\n"))
        quantity =int(input("Please enter the quantity:\n"))

        
        shoe_object = Shoes(country,code,product,cost,quantity)
        
        shoe_list.append(shoe_object)
       
        with open ("inventory.txt", "a") as shoe_file:

            shoe_file.writelines(f"\n{country},{code},{product},{cost},{quantity}")
    
        
        

# Define function
# Iterate over shoe_list
# Print out details using str method  
def view_all():
    
    with open("inventory.py","r+"):
        for item in shoe_list:
            print("\n")
            
            print(item.__str__())
            
            
            
# Define function 
# Find shoe object with lowest quantity
# Ask user to enter whether they want to re-stock and by how much
# Write updated quantity into inventory.txt
# Reference-https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/
def re_stock ():
    
    low_stock = shoe_list[0]
    
    for item in shoe_list:
        
        
        
      if int(item.get_quantity()) <= int(low_stock.get_quantity()):     
       low_stock=item
       
    print(f"\nThese shoes have the lowest quantity {low_stock}\n")
                     
    
    restock_item=input("Would you like to re-stock ? Please enter Yes or No ?\n")
    
    if restock_item=="Yes":
        
        
        
        edit_quantity= int(input("\nHow many would you like to re-stock with ?\n"))
        
        
        edit_stock= int(low_stock.quantity) + (edit_quantity)
        

        
        with open ("inventory.txt","r+") as file:
                    in_file = file.read()
                    in_file=in_file.replace(low_stock.quantity, str(edit_stock) + "\n")
                               
                      
        with open("inventory.txt","w") as write_file:
                    write_file.write(in_file)
                     
                    print(f"\nThis item has been restocked by {edit_quantity}")
              
                    
    else:
            print("You didn't restock this item.")
    
    
    
                    
              
  
        
# Define function
# Ask user to enter code of shoe
# Return the corresponding shoe from shoe_list
def search_shoe():
    
    code_search = input("Please enter the code of the shoe you wish to see:\n")
    
    for item in shoe_list:
        
    
    
      if item.code == code_search:
          print("\n")
          
          print(item)
   
    
    
    

# Define function
# Using value=cost*value formula
# Calculte the total value of each item in shoe_list
def value_per_item ():
    

    for shoe_item in shoe_list:
        value = int(shoe_item.cost) * int(shoe_item.quantity)
        
        print(f"The value of {shoe_item.product} is {value}") 
        
        
        
        
# Define function
# Determine index in shoe_list
# Store in variable called high_stock
# Condition of loop function to find highest quantity
# Print out high_stock 
# Print out that they are on sale
def highest_qty():
    
    
    
    high_stock=shoe_list[0]
    
    for item in shoe_list:
        
        
        if int(item.get_quantity()) >= int(high_stock.get_quantity()):
            
            high_stock=item
            
    print(f"The shoe with the highest quantity is : {high_stock}")
    
    print("\nThese shoes are on sale !")



# Create menu function 
# Call read_shoe_menu()
# Print menu        
def main_menu():
    read_shoe_data()
    
    


          
    print("""\n Welcome to our menu. Please see our options below:\n
        
            1- Capture inventory data 
            2- View all inventory 
            3- Item re-stock
            4- Search for item
            5- Price of item
            6- Highest quantity of item
            7- Quit menu \n""")


#Call menu function
#main_menu()

while True:
 main_menu()
# User to input an option in the menu
 user_option = input("\nPlease choose an option:\n")#.lower+ Quit option



    
     
 # Elif user selects 1
 # Call capture_shoes()       
 if user_option == "1":
     capture_shoes()
     


# Elif user selects 2
# Call view_all ()
 elif user_option == "2":
     view_all()
    
      
      
 # Elif user selects 3
 # Call re_stock ()     
 elif user_option == "3":
     re_stock()
     

# Elif user selects 4
# Call search_shoe function   
 elif user_option == "4":
     search_shoe()
     
       
# Elif user selects 5
# Call value_per_item()
        
 elif user_option == "5":
     value_per_item()
     
            
            
# Elif user selects 6
# Call function highest_qty()
 elif user_option == "6":
     highest_qty()
    
       

 #Elif user selects 7
 #User exits menu
 elif user_option == "7":
     print("You have exited the menu")
     exit()
     
     
        
 #Else user has not selected correcty.       
 else:
    print("You have not selected any of the options available to you. Please try again")
    
 