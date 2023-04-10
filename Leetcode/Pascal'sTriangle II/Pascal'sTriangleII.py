class Solution:
    def getRow(self, rowIndex: int) -> List[int]:  
        def factorial(number, result=1):
            for x in range(1, number+1):
                result *=x
            return result
        def calculation(n, p):
            calc = int(factorial(n) / (factorial(p)*(factorial(n-p))))
            return calc    
        control = [1]
        for x in range(1, rowIndex+1):
            control.clear()
            for y in range(rowIndex+2):
                element = calculation(x,y)
                if element==0:
                    pass
                else:
                    control.append(element)
        return control
