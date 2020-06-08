
f = [-1]*45
f[0]=1
f[1]=1

def fib(i):
    global f

    if i<=1:
        return f[i]
    if f[i] == -1:
        f[i] = fib(i-1)+fib(i-2)
    return f[i]

n=int(input())
print(fib(n))
