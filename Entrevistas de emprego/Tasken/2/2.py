def compress_string(string=input("Digite uma palavra para ser compactada:\n")):  
  compressed_string=""   
  counter=1  

  for x in range(1, len(string) + 1):  
    if x < len(string) and string[x] == string[x-1]:  
      counter += 1      
    else:  
      compressed_string+=string[x-1]  
      if(counter>1):  
        compressed_string+=str(counter)  
        counter=1   

  return compressed_string  

print(compress_string())