from itertools import combinations
from collections import deque
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = input()
    ns_R = 0
    ns_H = 0
    we_R = 0
    we_H = 0
    _l = []
    if len(a) == 2 and a[0] != a[1]:
        print("NO")
        continue
    last_moved = 0
    for e in a:
        match e:
            case "N":
                if ns_R == ns_H:
                    if last_moved == 0 or last_moved == "R":
                        _l += ("H",)
                        ns_H += 1
                    else:
                        _l += ("R",)
                        ns_R += 1
                elif ns_R < ns_H:
                    ns_R += 1
                    _l += ("R",)
                else:
                    ns_H += 1
                    _l += ("H",)
            case "S":
                if ns_R == ns_H:
                    if last_moved == 0 or last_moved == "R":
                        _l += ("H",)
                        ns_H -= 1
                    else:
                        _l += ("R",)
                        ns_R -= 1
                elif ns_R > ns_H:
                    ns_R -= 1
                    _l += ("R",)
                else:
                    ns_H -= 1
                    _l += ("H",)
            case "W":
                if we_R == we_H:
                    if last_moved == 0 or last_moved == "R":
                        _l += ("H",)
                        we_H -= 1
                    else:
                        _l += ("R",)
                        we_R -= 1
                elif we_R > we_H:
                    we_R -= 1
                    _l += ("R",)
                else:
                    we_H -= 1
                    _l += ("H",)
            case "E":
                if we_R == we_H:
                    if last_moved == 0 or last_moved == "R":
                        _l += ("H",)
                        we_H += 1
                    else:
                        _l += ("R",)
                        we_R += 1
                elif we_R <= we_H:
                    we_R += 1
                    _l += ("R",)
                else:
                    we_H += 1
                    _l += ("H",)
        last_moved = _l[-1]
    if ns_R != ns_H or we_R != we_H:
        print("NO")
    else:
        print("".join(_l))
