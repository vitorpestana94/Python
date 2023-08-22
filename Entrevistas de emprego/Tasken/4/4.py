def vowel_counter(): 

  file_ = input("Digite o nome do arquivo:\n") 
  vowel = "aeiouAEIOU" 
  consonants = " BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz" 
  vowel_dict = {} 
  consonants_dict = {}    

  try:      

    with open(file_, 'r') as file: 
      lines = file.readlines() 

      for v in range(len(lines)): 
        for a, b in enumerate(lines[v]): 
          if b == " " or b == "\n": 
            lines[v] = lines[v].replace(b, "") 

      for x in range(len(lines)): 
        vowel_counter=0 
        consonants_counter=0 

        for y,z in enumerate(lines[x]): 
          if z in vowel: 
            vowel_counter+=1 
            vowel_dict[x+1] = vowel_counter 
          elif z in consonants: 
            consonants_counter+=1 
            consonants_dict[x+1] = consonants_counter 

      vowel_line = sorted(vowel_dict.items(), key=lambda item: item[1]) 
      consonants_line = sorted(consonants_dict.items(), key=lambda item: item[1]) 

      print("\n-A linha que possui mais vogais é a linha {} com {} vogais\n-A linha que possui mais consoantes é a linha {} com {} consoantes.".format(vowel_line[-1][0], vowel_line[-1][-1], consonants_line[-1][0], consonants_line[-1][1])) 

  except FileNotFoundError: 
      print("ERROR!Arquivo não encontrado!") 

vowel_counter() 