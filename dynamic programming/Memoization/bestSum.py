
def bestSum(targetSum, numbers,memo={}):
    result = None
    if(targetSum < 0): return None
    if(targetSum == 0 ): return []
    if targetSum in memo: return memo[targetSum]
    for i in numbers:
        remainder = targetSum-i
        arr = bestSum(remainder, numbers,memo)
        if arr != None:
            temp = [*arr,i]
            if(result == None or len(temp) < len(result)):
                result = temp
    memo[targetSum] = result
    return result
print(bestSum(300,[7,14]))
print(bestSum(8,[2,3,5]))
print(bestSum(100,[1,2,5,25]))
