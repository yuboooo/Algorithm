def canSum(targetSum,numbers,memo={}):
    if(targetSum == 0): return True
    if(targetSum <0): return False
    if(targetSum in memo): return False # memo
    for i in numbers:
        remainder = targetSum - i
        if(canSum(remainder,numbers,memo) == True): return True
        else: memo[remainder] = False # memo
    
    return False


print(canSum(7,[5,3,4,7]))
print(canSum(8, [2,3,5]))
print(canSum(300, [7,14]))