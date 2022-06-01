from collections import deque

pump_q = deque()
n_pumps = int(input())

for _ in range(n_pumps):
    pump_info = list(int(x) for x in input().split())
    pump_q.append(pump_info)

for attempt in range(n_pumps):
    tank = 0
    failed = False
    for fuel, dist in pump_q:
        tank += fuel
        if dist > tank:
            failed = True
            break
        else:
            tank -= dist
    if failed:
        pump_q.append(pump_q.popleft())
    else:
        print(attempt)
        break