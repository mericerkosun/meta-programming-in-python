#Lists
list1 = [1,2,3,4,5]
print(*list1)
print(list1, sep= ",")

list1.insert(1,8) # With spesific index
print(*list1)

list1.append(3)
print(*list1)

list1.extend(["a","b","c"]) # Accepts a list
print(*list1)

list1.pop(0) # Remove spesific index
print(*list1)

del list1[2]
print(*list1) # Remove spesific index

for x in list1:
    print("Value",x)

# Tuples -> Immutable
my_tuple = (1, "string", "string", False)
my_tuple.count("string") # Belirtilen değerin tuple içinde kaç tane olduğunu verir.
my_tuple.index(False) # Belirtilen değerin indexini verir.

# Sets -> No duplicates, no indexes
my_set = {1, 2, 3, 4, 5}
my_set.add(7)
my_set.remove(1)
print(my_set)

# Dictionaries
my_dictionary = {1: "Meriç", 2:"Emre", 3: "Erkoşun"}
for key,value in my_dictionary.items():
    print(str(key) + " " + value)