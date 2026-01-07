#Dynamic Array
# python list grow
import sys
l1 = []
print("initial size",sys.getsizeof(l1))
for i in range(0,17):
    l1.append(i)
    print(f"{i} --> {sys.getsizeof(l1)}")
# -------------------------------------------
## homogenous or only a single type allowed
import sys
l1 = []
a=1
l1.append(1)
print(id(1))
print(id(a))
print(id(l1[0]))