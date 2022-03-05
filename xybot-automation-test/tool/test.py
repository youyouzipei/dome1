
s='123455'
a = []
b = 0
c = ""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        s1 = s[i:j]
        print(s1)
        if s1 not in c and len(s) == len(set(s)):
            a.append(s1)
            if len(s1) > b:
                b = len(s1)
                c = s1
    print("-------")

print('JIEGUO',b,c)