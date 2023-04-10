Class Solution:
  def romanToInt(self, s: str) -> int:
        InT = 0
        while len(s) != 0:
            if "CM" in s[:]:
                InT += 900
                s = s.replace("CM", "")
            elif "CD" in s[:]:
                InT += 400
                s = s.replace("CD", "")
            elif "XC" in s[:]:
                InT += 90
                s = s.replace("XC", "")
            elif "XL" in s[:]:
                InT += 40
                s = s.replace("XL", "")
            elif "IX" in s[:]:
                InT += 9
                s = s.replace("IX", "")
            elif "IV" in s[:]:
                InT += 4
                s = s.replace("IV", "", 1)
            elif "I" in s[:]:
                InT += 1
                s = s.replace("I", "", 1)
            elif "V" in s[:]:
                InT += 5
                s = s.replace("V", "", 1)
            elif "X" in s[:]:
                InT += 10
                s = s.replace("X", "", 1)
            elif "L" in s[:]:
                InT += 50
                s = s.replace("L", "", 1)
            elif "C" in s[:]:
                InT += 100
                s = s.replace("C", "", 1)
            elif "D" in s[:]:
                InT += 500
                s = s.replace("D", "", 1)
            elif "M" in s[:]:
                InT +=1000
                s = s.replace("M", "", 1)
        return InT
