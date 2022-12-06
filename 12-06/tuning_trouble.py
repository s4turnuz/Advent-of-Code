# Get data
def reader(file):
    return open(file).read()

# puzzle
def message(steps):  
    for (i, letter) in enumerate(f):                # get index
        if len(set(f[i:(i+steps)])) == steps:       # SET for don't duplicate in steps
            return i + steps

# main
f = reader('12-06/start-of-packet.txt')
print(message(4), message(14))
