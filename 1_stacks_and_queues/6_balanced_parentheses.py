expression = input()

balanced = True

opening_bracket = []

for ch in expression:
    if ch in "{[(":
        opening_bracket.append(ch)
    elif not opening_bracket:
        balanced = False
        break
    else:
        last_opening_bracket = opening_bracket.pop()
        if f'{last_opening_bracket}{ch}' not in '()[]{}':
            balanced = False
            break

if balanced and not opening_bracket:
    print("YES")
else:
    print("NO")