# find the largest  number
a,b,c=10,20,30
if a>=b and a>=c:
    print("a is largest")
if b>=a and b>=c:
    print("b is largest")
if c>=a and c>=b:
    print("c is largest")

print(max(a,b,c))