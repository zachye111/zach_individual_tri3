class Factor:

    def fact(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


n = int(input("Enter a number: "))
while n >= 1:
    obj = Factor()
    f = obj.fact(n)
    print("Factorial is of", n, "is", f)
    n -= 1