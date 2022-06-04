num_lines = int(input())
mendelei = set()
for _ in range(num_lines):
    my_list = input().split(' ')
    for i in my_list:
        mendelei.add(i)
print('\n'.join(mendelei))