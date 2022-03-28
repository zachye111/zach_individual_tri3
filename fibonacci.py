class Fib:
    def fact(self, n):
        if n<= 0:
            return "Incorrect Output"
        data = [0, 1]
        if n > 2:
            for i in range (2, n):
                data.append(data[i-1] + data[i-2])
        return data[n-1]


n = int(input("Enter a number: ")) + 1
while n >= 1:
    obj = Fib()
    f = obj.fact(n)
    print("Fib of", n - 1, "is", f)
    n -= 1