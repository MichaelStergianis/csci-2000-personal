

def has_no_e(line):
    for letter in line:
        if (letter is 'e'):
            return False
    return True

f = open("gadsby_stripped.txt")
for line in f:
    has_no_e(line)

f.close()
