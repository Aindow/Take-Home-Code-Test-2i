import re 
def getNums(str):
    nums = re.findall("\d",str)
    return map(int,nums)
def sum(numArray):
    total = 0 
    for int in numArray:
        total += int
    if total > 0:return total
def findMaxSum(array):
    maxNum = None 
    for str in array:
        num = sum(getNums(str))
        if maxNum == None : 
            maxNum = num
        elif num != None and num >= maxNum:
            maxNum = num
    return maxNum
def test():
    assert findMaxSum([ "dh7js4jf", "or2rjvn2w", "h1n36mfl", "a7e6fw" ]) ==  13, "Output should be 13"
    assert findMaxSum(["hjfdsuin","askjdh","dsjkhjg","asiuhhuif"]) == None, "Output should be None"
    assert findMaxSum(["huf789","8993dujui832","n89fwh8-113","fhh","","juir83"]) == 42, "Output should be 42"

test()
