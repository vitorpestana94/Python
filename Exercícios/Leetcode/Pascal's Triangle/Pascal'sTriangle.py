class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def factorial(number, result=1):
            for x in range(1, number+1):
                result *=x
            return result

        def calculation(n, p):
            calc = int(factorial(n) / (factorial(p)*(factorial(n-p))))
            return calc

        control = [1]
        final_array=[]
        for x in range(1, numRows+1):
            final_array.append(control.copy())
            control.clear()
            for y in range(numRows+1):
                elemento= calculation(x,y)
                if elemento==0:
                    pass
                else:
                    control.append(elemento)
        return final_array
