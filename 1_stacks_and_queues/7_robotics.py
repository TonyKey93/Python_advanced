robots = input().split(";")
for _ in robots:
    name,time = _.split('-')
    print(name, end = '')
    print(time)
