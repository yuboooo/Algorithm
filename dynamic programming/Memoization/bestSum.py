
def bestSum(targetSum, numbers,memo={}):
    result = None
    if(targetSum < 0): return None
    if(targetSum == 0 ): return []
    for i in numbers:
        remainder = targetSum-i
        arr = bestSum(remainder, numbers)
        if arr != None:
            temp = [*arr,i]
            if(result == None or len(temp) < len(result)):
                result = temp
    return result

print(bestSum(8,[2,3,5]))
            