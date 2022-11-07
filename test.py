def num_extract(s):
    num = []
    ope = []
    for i in s:
        if i in "0123456789":
            num.append(i)
        elif i in "+-*/":
            ope.append(i)
    if len(ope) + 1 == len(num):
        eq = [num[i] + ope[i] for i in range(len(ope))]+[num[-1]]
        value = eval(" ".join(eq))
        return value
    return s

print(num_extract("What is 1+2*3"))