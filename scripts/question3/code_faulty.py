global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            if local_variable in numbers:  # Check if local_variable exists before removing
                numbers.remove(local_variable)
        local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5}

# Corrected function call to match definition (no argument passed)
result = process_numbers()

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

# Removed the unnecessary argument from the function call
modify_dict()

def update_global():
    global global_variable
    global_variable += 10

# Removed the unnecessary 'i += 1' since the for loop already handles the increment
for i in range(5):
    print(i)

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met")  # Fixed typo from "Condidoin mety"

# Corrected the check to look for the string 'key5', not the integer 5
if 'key5' not in my_dict:
    print("Key 'key5' not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)
