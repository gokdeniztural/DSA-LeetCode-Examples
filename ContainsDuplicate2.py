nums = [3, 1, 4, 1, 5]

def solutions2():
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

print(solutions2())

'''
Burada hız  düşsse de hashset kullanarak bellekten ek bir yer ayırmadığımız için space complexity daha iyi bir durumda olacaktır.
Time Complexity -> O(nlogn)
'''

def solutions3():
    return len(nums) != len(set(nums))

print(solutions3())