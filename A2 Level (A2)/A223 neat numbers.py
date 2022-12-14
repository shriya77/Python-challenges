nums = []
neats = []

for i in range(101,1000):
    nums.append(i)
for i in range(899):
    checkdigit = nums[i]
    sums = 0
    for digit in str(checkdigit):
      sums += int(digit)
    remainder = int(checkdigit) % sums
    if remainder == 0:
        neats.append(checkdigit)

print(f" all the neat 3 digit numbers beginning with 101 up to 1000: {neats}")

