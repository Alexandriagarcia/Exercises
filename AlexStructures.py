#Structure of Ma. Alexandria P. Garcia


letters = ['m','a','a','l','e','x','a','n',
                'd','r','i','a','p','u','e','r',
                't','a','s','g','a','r','c',
                'i','a']


from collections import Counter
letters_counts = Counter(letters)
repeat = letters_counts.most_common(5)
print ("letters duplicated")
print(repeat)