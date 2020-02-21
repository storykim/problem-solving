import collections
nums = collections.deque(range(1, int(input())+1 ))

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())
print(nums[0])

