def Fibonacci(n):
    if n < 0 :
        print("invalid input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(7))



 #easy way to represent fibonacci no.

def Fibonacci(n):
    f = [0, 1]

    for i in range (2, n+1):
        f.append(f[i-1]+f[i-2])
    return f[n]

print(Fibonacci(4))





