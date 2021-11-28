class MyMath:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return print(self.a + self.b)

    def multiplication(self):
        return print(self.a * self.b)

    def division(self):
        try:
            self.a / self.b
        except ZeroDivisionError:
            print("MyMath error : You can't divide by zero.")
        else:
            return print(self.a / self.b)

    def subtraction(self):
        return print(self.a - self.b)

    def pow(self):
        return print(self.a ** self.b)

    def sqrt(self):
        if self.a < 0:
            print("MyMath error : You cannot take the root of a negative number.")
        else:
            return print(self.a ** 0.5)


ans = MyMath(4, 4)
ans.addition()
ans.subtraction()
ans.multiplication()
ans.division()
ans.pow()
ans.sqrt()
# print("1) +; 2) *; 3) /; 4) -; 5) pow; 6) sqrt; a, b = 4, 4")


print()


err = MyMath(-1, 0)
err.division()
err.sqrt()
# print("1) /; 2) sqrt; a, b = -1 0")
input("Press Enter to exit...")
