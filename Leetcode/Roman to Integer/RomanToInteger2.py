class Solution:
    def romanToInt(self, s: str) -> int:
      InT=0
      verbum=s
      simplex = {"I" : 1 ,"V" : 5 , "X":10, "L":50,
                "C": 100, "D": 500, 
                "M": 1000}
      
      compositis= {"IV":4, "IX": 9, "XL": 40,
                   "XC":90, "CD": 400, "CM": 900}
      
      for x in range(len(s)):
        if s[x:x+2] in compositis:
          InT+= compositis[s[x:x+2]]
          verbum=verbum.replace(s[x:x+2], "")
      
      for y in range(len(verbum)):
        if verbum[y] in simplex:
          InT+=simplex[verbum[y]]
      
      return InT
