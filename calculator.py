class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b # bug fixed

    def multiply(self, a, b):
        result = 0 
        if (b >= 0): # FIx bug
            for i in range(b):
                result = self.add(result, a)
            return result
        elif (a < 0 and b < 0):
            for i in range(abs(b)):
                result = self.add(result, abs(a))
            return result
        else:
            for i in range(abs(b)):
                result = self.add(result, -abs(a))
            return result
        

    def divide(self, a, b):
        result = 0
        if (a < 0 and b < 0): #bug fix
            a,b = abs(a), abs(b)
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return (result)
        elif (b < 0):
            b = abs(b)
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -abs(result)
        elif (a < 0):
            a = abs(a)
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -abs(result)
        elif (b == 0):
            return 'Undefined'  
        else:
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))