def caesarDecoder(str1):
    list1 = list(str1)
    for i in range(len(list1)):
        list1[i] = chr(ord(list1[i])-3)
    str1 = "".join(list1)
    return str1  



f1 = open("account.txt", "r")
for i in f1:
    print(i)