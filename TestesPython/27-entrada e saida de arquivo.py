my_list = [i ** 2 for i in range(1, 11)]
 Generates a list of squares of the numbers 1 - 10
f = open("output.txt", "w")
for item in my_list:
  f.write(str(item) + "\n")
f.close()
myfile = open("output.txt", "r+")
my_list = [i ** 2 for i in range(1, 11)]
my_file = open("output.txt", "w")
for value in my_list:
    my_file.write(str(value) + "\n")
my_file.close()

myfile = open("output.txt", "r")
print(myfile.read())
myfile.close

myfile = open("output.txt", "r")
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())
myfile.close

 Use a file handler to open a file for writing
write_file = open("text.txt", "w")

 Open the file for reading
read_file = open("text.txt", "r")

 Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

 Try to read from the file
print (read_file.read())

read_file.close()

with open("text.txt", "w") as textfile:
  textfile.write("Success!")

with open("text.txt", "w") as textfile:
    textfile.write("Vo fazer um program fodastico")

if not textfile.closed:
    textfile.close()
    
print(textfile.closed)    
