from collections import deque

def list_of_q(in_q):
    my_list = list(q)
    str_list = list(str(i) for i in my_list)
    return ' '.join(str_list)


is_running = True
q = deque()
orders = int(input())
in_str = input().split()
int_list = list(int(x) for x in in_str)
for i in int_list:
    q.append(i)
print(max(q))
while True:
    if q:
        if (orders - q[0]) < 0:
            print(f'Orders left: {list_of_q(q)}')
            break
        else:
            orders -= q.popleft()
    else:
        print("Orders complete")
        break
