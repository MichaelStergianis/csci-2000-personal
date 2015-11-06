# has_no_e iterates through a line provided by the parameter
# and checks each letter in the line to see if it is an 'e'
def has_no_e(line):
    for letter in line:
        if (letter is 'e'):
            return False
    return True

# You didn't ask us to output anything. 
# Do you want the program to print the result??
f = open("gadsby_stripped.txt")
for line in f:
    has_no_e(line)

f.close()
