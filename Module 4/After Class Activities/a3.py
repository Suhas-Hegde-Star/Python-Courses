def multiply_tuple(nums):
    product = 1
    for num in nums:
        product *= num
    return product

nums1 = (4, 3, 2, 2, -1, 18)
print("Product for", nums1, ":", multiply_tuple(nums1))

nums2 = (2, 4, 8, 8, 3, 2, 9)
print("Product for", nums2, ":", multiply_tuple(nums2))