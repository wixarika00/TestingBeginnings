values = [1, 2, "Aga", 4, 5]  # list is a data type that allows multipule values and can have differnet data type

print(values[0])

print(values[-1])
print(values[1:3])  # does not include the last index
values.insert(3, "Hydzik")
print(values)
values.append("End")
print(values)
values[2] = "AGA"  # Updating
print(values)

del values[0]  # deleting

print(values)

# list is mutable, you can change it, tuple is immutable
a = (1, 2, 3, 4)  # tuple
print(a)

print(a[1])

# Dictionary
dic = {"a": 2, 4: "bcd", "c": "Hello world"}
print(dic[4])
print(dic["c"])

#

dict = {}
dict["first_name"] = "Aga"

dict["last_name"] = "Hydzik"

print(dict)
print(dict["last_name"])




