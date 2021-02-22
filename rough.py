n = int(input())
lst = list(range(n+1))
abc = lst[1:n+1]
abc_str = map(str,abc)
out = "".join(abc_str)
print(out)
