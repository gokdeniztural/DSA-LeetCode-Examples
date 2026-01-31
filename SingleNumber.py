nums = [4, 1, 2, 1, 7, 2, 4]
# PROBLEM
# O(n) time complexity ve O(1) space complexity kullanılmalı.

def singleNumber():
    if len(nums) == 1:
        return nums[0] # edge case -> nums = [3] --> output: 3
    result = 0
    for num in nums:
        result = result ^ num 
    return result

print(singleNumber())

# XOR Operatörü ile binary şekilde karşılaştırma yaptık. -> "Bit Manipulation"
    






    
    