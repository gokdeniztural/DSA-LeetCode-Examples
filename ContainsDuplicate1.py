cnums = [1,3,2,4,7,9,9]

def containsDuplicate():
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False

print(containsDuplicate())

'''
Burada Time Complexity ve Space Complexity O(n) -> Hız kazanmak için bellekten harcadım.
'''