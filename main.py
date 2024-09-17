file=open("Codingal.txt","r")
print(file.read())
file.close()

#5read 5 characters
file=open("Codingal.txt","r")
print(file.read(5))
file.close()

#open the file in read mod
file=open("Codingal.txt","a")
print(file.write("My name is Breezy im from Gauteng"))
file.close()

#read first line
file=open("Codingal.txt","r")
print(file.readline())
file.close()



#read 3 lines
file=open("Codingal.txt","r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

#loop
file=open("Codingal.txt","r")
for line in file:
    print(line)
file.close