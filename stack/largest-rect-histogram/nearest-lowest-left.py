def nearesetLowestLeft(ip):
    stack = []
    span = []

    # find the nearest greatest to the left
    for idx, num in enumerate(ip):

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
    print(span)


nearesetLowestLeft([100,80,60,70,60,75,85])
# nearesetLowestLeft([100, 80, 110, 90, 60, 70, 95])
