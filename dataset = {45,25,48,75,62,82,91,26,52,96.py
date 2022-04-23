dataset = {45,25,48,75,62,82,91,26,52,96,40,60,61,82,72,60}
a = 0
b = 0
c = 0
d = 0
f = 0

for z in dataset:
    if z >= 80:
        a=a+1
    elif z >= 70:
        b=b+1
    elif z >= 60:
        c=c+1
    elif z >= 50:
        d=d+1
    else:
        f=f+1
print("Number of Student have grade A = " + str(a))
print("Number of Student have grade B = " + str(b))
print("Number of Student have grade C = " + str(c))
print("Number of Student have grade D = " + str(d))
print("Number of Student have grade F = " + str(f)) 