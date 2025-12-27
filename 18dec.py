#Двумерные массивы
#1
"""with open('39762.txt') as f:
    nums = list(map(int, f.read().split()))

count = 0
max_sum = 0

for i in range(len(nums) - 1):
    prod = nums[i] * nums[i + 1]
    s = nums[i] + nums[i + 1]

    if prod % 15 == 0 and s % 7 == 0:
        count += 1
        if s > max_sum:
            max_sum = s

print(count, max_sum)"""
#2

"""with open('68279.txt') as f:
    nums = list(map(int, f.read().split()))

max_562 = max(x for x in nums if x % 1000 == 562)

count = 0
max_sum = 0

for i in range(len(nums) - 3):
    four = nums[i:i + 4]

    five_digit = sum(1 for x in four if 10000 <= x <= 99999)
    if not (five_digit >= 1 and five_digit <= 2):
        continue

    mod3 = sum(1 for x in four if x % 3 == 0)
    mod7 = sum(1 for x in four if x % 7 == 0)
    if mod3 >= mod7:
        continue

    s = sum(four)
    if max_562 < s < 2 * max_562:
        count += 1
        if s > max_sum:
            max_sum = s

print(count, max_sum)"""

#3

with open('40992.txt') as f:
    nums = list(map(int, f.read().split()))

odd_nums = [x for x in nums if x % 2 != 0]
avg_odd = sum(odd_nums) / len(odd_nums) if odd_nums else 0

count = 0
max_sum = 0

for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]

    if (a % 5 != 0) and (b % 5 != 0):
        continue

    if a >= avg_odd and b >= avg_odd:
        continue

    count += 1
    if a + b > max_sum:
        max_sum = a + b

print(count, max_sum)