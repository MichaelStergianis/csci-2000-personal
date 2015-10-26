writer = open("temp.txt", 'w')
writer.write("elements\n")
elements = ['He', 'Ne', 'Ar', 'Kr']
for i in elements:
    writer.write(i + '\n')
writer.close()
