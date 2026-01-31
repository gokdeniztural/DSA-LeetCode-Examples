nums = [2, 2, 1, 1, 1, 2, 2]

def boyerMoore():
    result = 0
    count = 0

    for num in nums:
        if count == 0:
            result = num
        if num == result:
            count +=1
        else:
            count -=1
    return result

print(boyerMoore())