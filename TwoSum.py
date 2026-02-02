nums = [2,7,11,15]
target = 9 # test

def twoSum():
    result = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in result:
            return [result[complement], i]
        else:
            result[num] = i

print(twoSum())