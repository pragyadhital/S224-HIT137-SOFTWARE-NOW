global_variable = 100  # Fixed typo: 'global_varaible' -> 'global_variable'
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):  # Fixed typo: 'proess_numbers' -> 'process_numbers'
    global global_variable  # Fixed typo: 'global_varaible' -> 'global_variable'
    local_variable = 5  # Fixed typo: 'local_varaible' -> 'local_variable'
    numbers_list = list(numbers) 

    while local_variable > 0:
        if local_variable % 2 == 0:
            if local_variable in numbers_list:  
                numbers_list.remove(local_variable)
        local_variable -= 1

    return numbers_list  

my_set = {1, 2, 3, 4, 5} 
result = process_numbers(numbers=my_set)  

def modify_dict():
    local_variable = 10  # Fixed typo: 'local_varaible' -> 'local_variable'
    my_dict['key4'] = local_variable

modify_dict() 

def update_global():  # Fixed typo: 'upnate_global' -> 'update_global'
    global global_variable
    global_variable += 10

update_global()  # Added this line to call the 'update_global' function

for i in range(5):
    print(i)
    # i += 1  # Removed the manual increment of 'i', as the for loop automatically increments 'i'

# Check if the set is not None and if the value of 'key4' in the dictionary is 10
if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")
# Check if the number 5 is not a key in the dictionary (original code had '5 not ford' typo)
if 5 not in my_dict:
    print("5 not found in the dictionary!")  # Fixed typo: 'ford' -> 'found'

print(global_variable)  
print(my_dict) 
print(my_set)  
