# dict
my_dict = {"Tsunami": 7, "Earthquake": 300, "Eruption": 43}
print(my_dict)
print("Tsunami:", my_dict['Tsunami'])
print(my_dict.get('Eclipse'))
my_dict.update({"Quarantine": 0,
                "Zombie apocalypse": 2})
print(my_dict)
z_a = my_dict.pop("Zombie apocalypse")
print("Popped valuable:", z_a)
print(my_dict, '\n')
# set
my_set = {59, "name", 'name', 59.2, (1, 2, 3, 4), (1, 2, 3, 4), 59, "duck"}
print(my_set)
my_set.add("O")
my_set.add(0)
print(my_set)
my_set.discard((1, 2, 3, 4))
print(my_set)
