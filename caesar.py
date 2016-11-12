import cs50
import sys

if len(sys.argv)!=2:
      print("Usage: ./caesar key")
      exit(1)
else:
    key=int(sys.argv[1])  
    print("plaintext: ", end="")
    string=cs50.get_string()
    result=[]
    for i in range(len(string)):
        if (string[i].isupper()):
            result.append(chr((((ord(string[i]) - ord('A')) + key) % 26) + ord('A')))
        else:
            result.append(chr((((ord(string[i]) - ord('a')) + key) % 26) + ord('a')))
    print("ciphertext: ", end ="")
    print("".join(result)) 
      
    
    

    