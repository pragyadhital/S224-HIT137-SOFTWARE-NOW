global_varaible = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def proess_numbers():
    global global_varaible
    local_varaible = 5
    numbers = [1, 2, 3, 4, 5]

    while local_varaible > 0:
        if local_varaible % 2 == 0:
            numbers.remove(local_varaible)
        local_varaible -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(numbers=my_set)

def modify_dict():
    local_varaible = 10
    my_dict['key4'] = local_varaible

modify_dict(5)

def upnate_global():
    global global_varaible
    global_varaible += 10

for i in range(5):
    print(i)
    i += 1

if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")
if 5 not in my_dict:
    print("5 not ford in the dictionary!")
print(global_varaible)
print(my_dict)
print(my_set)