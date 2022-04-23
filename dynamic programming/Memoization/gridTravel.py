
# gridTravel in recursive
def gridTravel(n,m):
    if(n==0 or m==0): return 0
    elif(n == 1 and m == 1): return 1
    return gridTravel(n-1,m) + gridTravel(n,m-1)

print(gridTravel(3,3))

# gridTravel in dynamic, just add memoization
def dynamic(n,m,memo={}):
    key = str(m) +","+str(n)
    if (key in memo): return memo[key]
    if(n==0 or m==0): return 0
    elif(n == 1 and m == 1): return 1
    memo[key] = dynamic(n-1,m,memo) + dynamic(n,m-1,memo)
    return memo[key]

print(dynamic(18,18))