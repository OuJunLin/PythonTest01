def caesarEncoder(str1):
    list1 = list(str1)
    for i in range(len(list1)):
        list1[i] = chr(ord(list1[i])+3)
    str1 = "".join(list1)
    return str1
        
def caesarDecoder(str1):
    list1 = list(str1)
    for i in range(len(list1)):
        list1[i] = chr(ord(list1[i])-3)
    str1 = "".join(list1)
    return str1  



def leaveMessage(account,str1):
    f = open("messageFile.txt","a")
    str1 = caesarEncoder(str1)
    account = caesarEncoder(account)
    f.write("{} {} {}\n" .format(account,caesarEncoder(":"), str1))
    f.close()
    
def readMessage():
    f = open("messageFile.txt","r")
    for i in f:
        print(caesarDecoder(i))
    f.close()
   
    
    
def checkAccount(account,password):
    f = open("account.txt","r")
    
    f.close()



if __name__ == "__main__":
    leaveMessage("jack", "test")
    readMessage()
    


    

    