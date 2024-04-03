# the with statement will automatically close the file
# when it is finished with it
# Author: Grace Mary Smyth

with open("test-d.txt", "w") as f:
    data = f.write("test b\n") # returns no of characters written
    print (data)

with open("test-d.txt", "a") as f2: #open file again
    data = f2.write("another line\n")
    print (data)

# old way of doing this is
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()