import time
def fib(n):
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    # return fib(n - 1) + fib(n - 2)

    if n <= 1:
        return n
    
    grandparent = 0
    parent = 1
    for i in range(n - 1):
        current = grandparent + parent
        grandparent = parent
        parent = current
    return current


def fib_fast(n: int) -> int:
    def helper(k: int):
        # returns (F(k), F(k+1))
        if k == 0:
            return (0, 1)
        a, b = helper(k >> 1)          # a=F(m), b=F(m+1), m=k//2
        c = a * ((b << 1) - a)         # F(2m)
        d = a * a + b * b              # F(2m+1)
        if k & 1:
            return (d, c + d)          # (F(2m+1), F(2m+2))
        else:
            return (c, d)              # (F(2m), F(2m+1))

    return helper(n)[0]


if __name__ == "__main__":
    n = int(input())
    
    # time for fib vs fib_fast
    start = time.time()
    print(fib(n))
    end = time.time()
    print(f"Execution time: {end - start} seconds")

    start = time.time()
    print(fib_fast(n))
    end = time.time()
    print(f"Execution time: {end - start} seconds")

