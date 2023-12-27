def more_one(nums):
    return sorted([x for x in set(nums) if nums.count(x) > 1])


nums = list(map(int, input().split()))
print(*more_one(nums))
