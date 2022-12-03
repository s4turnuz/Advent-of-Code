from string import ascii_lowercase, ascii_uppercase

# Get data
f = open('12-03/rucksacks.txt').read()

# First method :P... it's wrong... or harder

# dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
# dict2 = {'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}

elf_points = 0

# For some results practice

# ruck1 = "BdbzzddChsWrRFbzBrszbhW"
# ruck2 = "MLNJHLLLLHZtSLglFNZHLJH"

for line in f.split("\n"):

    ruck1 = line[:len(line)//2]
    ruck2 = line[len(line)//2:]

    x = set(ruck1).intersection(set(ruck2))

    for i in x:
        if i in ascii_lowercase:
            elf_points += ascii_lowercase.index(i) + 1
        elif i in ascii_uppercase:
            elf_points += ascii_uppercase.index(i) + 27

print(elf_points)
elf_points = 0


## PART TWO


f = f.split("\n")

for i in range(0, len(f), 3):

    commun = set(ascii_lowercase).union(set(ascii_uppercase))

    for j in range(i, i+3):
            commun = commun.intersection(set(f[j]))

    for i in commun:
        if i in ascii_lowercase:
            elf_points += ascii_lowercase.index(i) + 1
        elif i in ascii_uppercase:
            elf_points += ascii_uppercase.index(i) + 27


print(elf_points)