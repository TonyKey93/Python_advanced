# You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is one of these four types:
#· '1 {number}' – push the number (integer) into the stack
#· '2' – delete the number at the top of the stack
#· '3' – print the maximum number in the stack
#· '4' – print the minimum number in the stack
#It is guaranteed that each query is valid.
#After you go through all the queries, print the stack from top to bottom in the following format:
#{n}, {n1}, {n2}, ... {nn}"
N = int(input())
q = []
top_q = []
for i in range(N):
    cmd = input().split()
    if cmd[0] == '1':
        q.append(int(cmd[1]))
    elif cmd[0] == '2':
        if q: q.pop()
    elif cmd[0] == '3':
        if q: print(max(q))
    elif cmd[0] == '4':
        if q: print(min(q))

while q:
    top_q.append(q.pop())
print(', '.join( [str(int) for int in top_q]))
