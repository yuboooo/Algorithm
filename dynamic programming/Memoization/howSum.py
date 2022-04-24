def howSum(targetSum,numbers,memo = {}):
    if(targetSum < 0): return None
    if(targetSum == 0): return []
    if targetSum in memo: return memo[targetSum]
    for i in numbers:
        remainder = targetSum - i
        arr = howSum(remainder,numbers,memo)
        if(arr != None): 
            arr.append(i)
            return arr
        else: memo[remainder] = None
    return None


print(howSum(7,[5,3,4,7]))
print(howSum(8, [2,3,5]))
print(howSum(7,[2,4]))
print(howSum(300,[7,14]))