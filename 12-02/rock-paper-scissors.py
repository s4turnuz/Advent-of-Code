# Get data
f = open('12-02\elf_sequence.txt').read()

# Defeat 0
# Draw 3
# Win 6

# Rock          A   X   1
# Paper         B   Y   2
# Scissors      C   Z   3

my_points = 0

for line in f.split("\n"):
    elf, me = line.split()

    if me == "X":
        if elf == "C":
            my_points += 6
        if elf == "A":
            my_points += 3
        my_points += 1

    if me == "Y":
        if elf == "A":
            my_points += 6
        if elf == "B":
            my_points += 3
        my_points += 2

    if me =="Z":
        if elf == "B":
            my_points += 6
        if elf == "C":
            my_points += 3
        my_points += 3


print(my_points)
my_points = 0

# PART TWO

for line in f.split("\n"):
    elf, me = line.split()

    if me == "X":
        if elf == "A":
            my_points += 3
        if elf == "B":
            my_points += 1
        if elf == "C":
            my_points += 2
        
        my_points += 0

    if me == "Y":
        if elf == "A":
            my_points += 1
        if elf == "B":
            my_points += 2
        if elf == "C":
            my_points += 3
        my_points += 3

    if me =="Z":
        if elf == "A":
            my_points += 2
        if elf == "B":
            my_points += 3
        if elf == "C":
            my_points += 1
        my_points += 6

print('------ PART TWO ------')
print(my_points)
