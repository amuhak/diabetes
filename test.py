def test(a):
    if not len(set(a)) == 4:
        return False
    temp = sorted(a)
    temp.reverse()
    return temp == list(a)


ans = 0
l = set()
for i in range(1000, 10000):
    if test(str(i)):
        ans = ans + 1
        l.add(i)
print(ans)
print(len(l))
print(sorted(l))
