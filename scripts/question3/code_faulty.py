# Initialize a global variable
global_variable = 100  # Fixed typo: 'global_varaible' -> 'global_variable'

# Initialize a dictionary with key-value pairs
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Function to process numbers and remove even numbers less than or equal to 5 from the list
def process_numbers(numbers):  # Fixed typo: 'proess_numbers' -> 'process_numbers'
    global global_variable  # Use the global variable 'global_variable' within this function
    local_variable = 5  # Local variable initialized to 5
    numbers_list = list(numbers)  # Convert the input set into a list for modification

    # Loop until local_variable becomes 0
    while local_variable > 0:
        # If the local variable is even
        if local_variable % 2 == 0:
            # If the local variable is present in the list, remove it
            if local_variable in numbers_list:  
                numbers_list.remove(local_variable)
        local_variable -= 1  # Decrement the local variable by 1 on each iteration

    return numbers_list  # Return the modified list of numbers

# Create a set of numbers
my_set = {1, 2, 3, 4, 5} 

# Call the 'process_numbers' function with the set as input
result = process_numbers(numbers=my_set)  

# Function to modify the global dictionary by adding a new key-value pair
def modify_dict():
    local_variable = 10  # Local variable initialized to 10
    my_dict['key4'] = local_variable  # Add a new key-value pair ('key4': 10) to 'my_dict'

# Call the 'modify_dict' function to update the dictionary
modify_dict() 

# Function to update the global variable
def update_global():  # Fixed typo: 'upnate_global' -> 'update_global'
    global global_variable  # Use the global variable 'global_variable' within this function
    global_variable += 10  # Increment the global variable by 10

# Call the 'update_global' function to modify the global variable
update_global()

# Loop to print numbers from 0 to 4
for i in range(5):
    print(i)  # Print the current value of 'i'
    # i += 1  # Removed manual increment since the for loop automatically increments 'i'

# Check if the set 'my_set' is not None and the value of 'key4' in 'my_dict' is 10
if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")  # Print a message if both conditions are satisfied

# Check if the number 5 is not a key in 'my_dict'
if 5 not in my_dict:
    print("5 not found in the dictionary!")  # Print a message if 5 is not a key in the dictionary

# Print the final value of the global variable
print(global_variable)  

# Print the contents of the dictionary
print(my_dict) 

# Print the contents of the set
print(my_set)  
