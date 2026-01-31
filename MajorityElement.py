nums = [2,2,1,1,1,2,2,1,2,3,3,2,2]

def MajorityElement():
    counts = {}
    max = len(nums) // 2

    for num in nums:
        if num in counts:
            counts[num] += 1 # counts = {2:4 , 1:3}
        else:
            counts[num] = 1
    
        if counts[num] > max:
            return num
    
print(MajorityElement())

# Time Complexity: O(n)
# Space Complexity: O(n)