rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
]

#print out the total length of all the rivers.
total = 0

for river in rivers:
    total += river["length"]

print(total)

#print out the name of the rivers
for river in rivers:
    print(river["name"])

#print out and calculate the mean of the rivers.
mean_length = total / len(rivers)
print(mean_length)

#print out every river name that begins with the letter M
for river in rivers:
    if(river["name"][0] == "M"):
        print(river["name"])

#The length of the river names are in miles.
#print out the river length from miles to km (1 mile = 1.6km)
for river in rivers:
    print(river["length"] * 1.6)
