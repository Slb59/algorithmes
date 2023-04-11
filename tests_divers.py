def main():
    print("ok")

def fun(n):
    if (n==0):
        return
    
    print(n%2)
    fun(n//2)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
            return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
   j=0
   fib(9)
   print(j)