class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        if (a < 0) and (b < 0):
            a = abs(a)
            b = abs(b)
            result = 0
            for i in range(b):
                result = self.add(result, a)
            return result
        elif (a < 0) and (b > 0):
            a = abs(a)
            result = 0
            for i in range(b):
                result = self.add(result, a)
            return -result
        elif (a > 0) and (b < 0):
            b = abs(b)
            result = 0
            for i in range(b):
                result = self.add(result, a)
            return -result
        else:
            result = 0
            for i in range(b):
                result = self.add(result, a)
            return result

        # result = 0
        # for i in range(b):
        #     result = self.add(result, a)
        # return result

    def divide(self, a, b):
        if (a < 0) and (b < 0):
            a = abs(a)
            b = abs(b)
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
        elif (a > 0) and (b < 0):
            b = abs(b)
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -result
        elif (a < 0) and (b > 0):
            a = abs(a)
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -result
        else:
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result

            # result = 0
            # while a >= b:
            #     a = self.subtract(a, b)
            #     result += 1
            # return result

    def modulo(self, a, b):
        while a > b:
            if (b == 0):
                break
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
