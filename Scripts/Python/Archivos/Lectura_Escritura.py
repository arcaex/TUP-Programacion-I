
# Leer un archivo
with open('./ww200.txt', 'r') as file:
    data = []
    data = file.read().split("\n")

output_array = []

for element in data:
    first = element[0:257]
    second = " 0000000000000000"
    final = first + second
    output_array.append(final)

output = open("ww200-output","w")
for line in output_array:
    output.write(line + "\n")
output.close()
