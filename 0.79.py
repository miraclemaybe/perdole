nums = []

for i in range(3):
    n = int(input('chisla'))
    nums.append(n)
nums.reverse()
print(nums)

a = input('hochesh ostavit poslednuu cifru?(yes or no)')
if a == 'no':
    nums.pop(-1)
    print(nums)
elif a == 'yes':
    print(nums)