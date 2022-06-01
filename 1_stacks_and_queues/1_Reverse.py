nums = input().split()
my_stk = []
finish = []
for i in nums:
    my_stk.append(i)
while my_stk:
    finish.append(my_stk.pop())
print(' '.join(finish))