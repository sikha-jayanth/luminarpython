
#program to print fibonacci series


sum=0
fn=1
n=int(input("enter the limit"))          #n=4
for i in range(0,n):                     #i=0      i=1      i=2        i=3
    print(sum)                           #print 0  print 1   print 1   print 2
    fp = fn                              #fp=1     fp=0      fp=1       fp=1
    fn = sum                             #fn=0     fn=1      fn=1       fn=2
    sum=fp+fn                            #sum=1    sum=1     sum=2       sum=3



