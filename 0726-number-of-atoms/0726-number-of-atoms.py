class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def val(s):
            if s =="":
                return 1
            else:
                return int(s)

        l = len(formula)
        ms = deque()
        elements = defaultdict(int)
        name = ""
        count = ""
        multiplier = 1
        # Read and parse backwards, will give us counts before 
        # atom names or brackets

        # Atom names ends with capital letters when read backwards

        # The only extra information we need when scanning inside brackets
        # is the current multiplier

        for i in range(l-1,-1,-1):
            c = formula[i]
            if c.isupper():
                name = c+name
                elements[name] += val(count)*multiplier
                name = ""
                count = ""
            elif c.islower():
                name = c+name
            elif c.isdecimal():
                count = c+count
            elif c == ")":
                ms.append(multiplier)
                multiplier *= val(count)
                count = ""
            else: # "("
                multiplier = ms.pop()

        # now sort and join as string answer
        e = [s+str(n) if n>1 else s for s,n in elements.items()]
        e.sort()

        return "".join(e)        