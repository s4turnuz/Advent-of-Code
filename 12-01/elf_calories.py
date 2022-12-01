# Get Input file
f = open('elf_food.txt', 'r')

lines = f.readlines()

#print(type(lines))

# Some variables for data control
array = []
x = 0

for i in lines:
    if i == "\n":
        array.append(x)
        x = 0
    else:
        x = x + int(i)


## base values
value_first = array[0]
value_second = array[0]
value_third = array[0]

# 1 value
for j in array:
    if value_first <= j:
        value_first = j

print(value_first)
array.remove(value_first) 

# 2 value
for k in array:
    if value_second <= k:
        value_second = k

print(value_second)
array.remove(value_second)

# 2 value
for l in array:
    if value_third <= l:
        value_third = l

print(value_third)
array.remove(value_third)

sum_total = value_first + value_second + value_third

print(sum_total)

f.close()
