#Arrays and Function of Ma. Alexandria P. Garcia

a = input ("Enter a palindrome:")
fram = 1
red = 0
blue = 1
while True:
    if (red > int (len(a))):
        break
    if (blue > int (len(a))):
        break

    c = a[red]
    red += 1
    d = a[-blue]
    blue += 1

    if (c != d):
        fram = 0

if (fram == 0):
    print (a, "NOT A PALINDROME")
     
elif (fram == 1):
    print (a, "ITS A PALINDROME")
