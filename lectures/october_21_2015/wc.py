reader = open ('haiku.txt', 'r')
count = 0
data = reader.read(64)
while not (reader.eof()):
    count += len(data)
    data = reader.read(64)
count += len(data)
print(count)
reader.close()
