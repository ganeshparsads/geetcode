def nearesetLowestRight(ip):
    stack = []
    span = []

    size = len(ip)

    # find the nearest greatest to the left
    for idx, num in enumerate(reversed(ip)):

        # if num == 70:
        #     import pdb
        #     pdb.set_trace()

        if not stack:
            stack.append([num, idx])
            span.append(idx + 1)
            continue

        if stack[-1][0] < num:
            span.append(idx - stack[-1][1])
            stack.append([num, idx])
        else:
            while stack and stack[-1][0] >= num:
                stack.pop()

            if not stack:
                span.append(idx + 1)
            else:
                span.append(idx - stack[-1][1])

            stack.append([num, idx])

    print(ip)
    print(list(reversed(span)))


nearesetLowestRight([100, 80, 60, 70, 60, 75, 85])
# nearesetLowestRight([100, 80, 110, 90, 60, 70, 95])
