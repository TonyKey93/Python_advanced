def add_fun(in_set):
    if data_in[1] == "First":
        for m in data_in[2:]:
            set1.add(m)
    else:
        for m in data_in[2:]:
            set2.add(m)
    return


def rem_fun(in_set):
    if data_in[1] == "First":
        for m in data_in[2:]:
            if set1.__contains__(m):
                set1.remove(m)
    else:
        for m in data_in[2:]:
            if set2.__contains__(m):
                set2.remove(m)
    return


set1 = set(input().split(' '))
set2 = set(input().split(' '))
N = int(input())
for _ in range(N):
    data_in = input().split(' ')
    if data_in[0] == "Add":
        add_fun(data_in)
    elif data_in[0] == "Remove":
        rem_fun(data_in)
    elif data_in[0] == "Check" and data_in[1] == "Subset":
        is_subset = False
        if set1.issubset(set2):
            is_subset = True
        elif set2.issubset(set1):
            is_subset = True
        print(is_subset)

print(', '.join(sorted(set1)))
print(', '.join(sorted(set2)))
