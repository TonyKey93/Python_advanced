clothes = list(int(i) for i in input().split())
racks = 1
rack = int(input())
curr_rack = rack

while clothes:
    piece_of_clothing = clothes[-1]
    if piece_of_clothing > curr_rack:
        racks += 1
        curr_rack = rack
    else:
        curr_rack -= piece_of_clothing
        clothes.pop()

print(racks)
