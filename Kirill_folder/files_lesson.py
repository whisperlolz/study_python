# data = input("Write down your text: ")
#
# file = open('file.txt', 'a')
#
# file.write(data + "\n")
#
# file.close()

file = open('file.txt', 'r')

print(file.read(1))

file.close()
