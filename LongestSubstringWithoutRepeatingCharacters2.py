import itertools

s="abcbcb"
def main(s):
    max = 0
    # check all possible substrings
    for i in range(len(s)):
        for j in range(i, len(s)):
            foo=s[i:j+1]
            skip = False
            # check if this substring is non-repeating
            for a in range(len(foo)):
                skip2 = False
                for b in range(a+1,len(foo)):
                    if foo[a]==foo[b]:
                        # move on to the next substring
                        skip = True
                        skip2 = True
                        break
                if skip2:
                    break
            if skip:
                continue
            #substring is non-repeating
            print(foo)     
            if max<len(foo):
                max=len(foo)
    return max

def isNonRepeating(s):
    for a,b in itertools.product(s,s):
        print(a,b)

print(main("sdfjkweoisfj"))