memo = [0,1]
def fib(n):
    for i in range(2,n+1):
        memo.append(memo[i-1]+memo[i-2])
    return memo[n]

print(fib(50))

# fib in recursive way
def fibrecursive(n):
    if(n<=2): return 1
    return fibrecursive(n-1)+fibrecursive(n-2)

print(fibrecursive(7))

# fib in dynamic, just add memoization
def fib2(n,memo={}):
    if(n<=2): return 1
    if n in memo: return memo[n]
    memo[n] = fib2(n-1,memo)+fib2(n-2,memo)
    return memo[n]

print(fib2(50))
print(memo)