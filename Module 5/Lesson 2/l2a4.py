class pairlimets:
    def two_sum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return (num_dict[target - num], i)
            num_dict[num] = i

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
value = int(input("Enter the target sum: "))
print("Index 1 = %d,           Index 2 = %d" % pairlimets().two_sum((lst), value))