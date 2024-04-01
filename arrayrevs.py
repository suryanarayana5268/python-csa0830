import array as arr
new=arr.array('i',[1,2,3,4,5,6,7,8,9])
for i in range(len(new)-1,-1,-1):
  print(new[i],end="\t")