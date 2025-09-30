import sys

print("total no of argments:",len(sys.argv))
for i in sys.argv:
	print("argments",i)
a=int(sys.argv[1])
b=int(sys.argv[2])
sum=a+b
print("sum:",sum)