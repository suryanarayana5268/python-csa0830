import array as arr
a=arr.array('i',[1,2,6,7,5,4,3])
b=a.tolist()
b.sort()
a=arr.array('i')
a.fromlist(b)
print(" sorted array:", a)