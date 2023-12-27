import sys

nums = list(map(int, sys.stdin))
l = len(nums)

if all(map(lambda i: nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1], range(l - 2))):
    sys.stdout.write('Арифметическая прогрессия')
elif all(map(lambda i: nums[i + 1] // nums[i] == nums[i + 2] // nums[i + 1], range(l - 2))):
    sys.stdout.write('Геометрическая прогрессия')
else:
    sys.stdout.write('Не прогрессия')
