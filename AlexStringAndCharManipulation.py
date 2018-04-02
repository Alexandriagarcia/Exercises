#String And Char Manipulation of Ma. Alexandria P. Garcia

str = "Computer Engineering"

print("String is %d bytes long" % len(str))

print(str.upper())

print("The index of the o is %d" % str.upper().index("O"))

print("There are %d letter E's in '%s'" % (str.upper().count("E"), str))

#slice the string
print(str[3])
print(str[1:6])
print(str[1:len(str)])

name = "Alexandria Garcia"
mylist = name.split(" ")
print(mylist)
print("First Name : %s and Last Name : %s" %(mylist[0],mylist[1]))
